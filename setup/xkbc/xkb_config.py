# vim:set et sts=4 sw=4:
#
# ibus-xkbc - The Input Bus Keyboard Layout emulaton engine.
#
# Copyright (c) 2009-2010 Sun Microsystems, Inc All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sys
import os

# constants
from constants import *
# component token parser
from parser import *
from xkb_symbols import *
from xkb_types import *
from xkb_keycodes import *
from xkb_keymap import *
from xkb_geometry import *
from unicodeutil import *

DEFAULT_XKB_DATA_DIR = os.getenv('XKB_DATA_DIR')

# XKB Config database
class XKBCDB:

    def __init__(self, dir = DEFAULT_XKB_DATA_DIR, type = TYPE_ALL):
        self.symbols_dict = None
        self.keycodes_dict = None
        self.types_dict = None
        self.geometry_dict = None
        self.keymap_dict = None

        if type & TYPE_SYMBOLS:
            self.symbols_dict = SymbolsParser(dir).get_components()
            self.default_symbols_dict = self.select_default_symbols(self.symbols_dict)
            self.symbol_subdirs = self.select_subdirs(self.symbols_dict.keys())
        if type & TYPE_KEYCODES:
            self.keycodes_dict = KeycodesParser(dir).get_components()
        if type & TYPE_TYPES:
            self.types_dict = TypesParser(dir).get_components()
        if type & TYPE_GEOMETRY:
            self.geometry_dict = GeometryParser(dir).get_components()
        if type & TYPE_KEYMAP:
            self.keymap_dict = KeymapParser(dir).get_components()

    def select_default_symbols(self, sym_dict):
        dd = {}
        for v in sym_dict.values():
            hint = v.get_hint()
            if hint & HINT_DEFAULT:
                name = v.get_name()
                i = name.find(NAME_START)
                if i != -1:
                    name = name[:i]
                dd[name] = v
        return dd

    def select_subdirs(self, keys):
        ret_array = []
        for k in keys:
            names = k.split("/")
            if len(names) > 1 and (not names[0] in ret_array):
                ret_array.append(names[0])
        return ret_array

    search_order_list = [[REPLACE_DICT, REPLACE_LIST], [OVERRIDE_DICT, OVERRIDE_LIST],
                         [MAIN_DICT, INCLUDE_LIST], [AUGMENT_DICT, AUGMENT_LIST]]
    # public interface

    # Returns 'keyname' corresponding 'keysym' in symbol_name
    # 'keyname' is string like "<AE01>"
    #
    # 'symbol_name' is string like "fr" or "fr(latin9_sundeadkeys)" 
    # 'keysym' is string like 'a', 'tilda'
    # 'group' and 'level' is the same meaning in XKB spec
    def search_key_name(self, symbol_name, keysym, state):
        sym_dict = self._get_sym_dict(symbol_name)
        key_name = self._get_key_name(sym_dict, keysym, state)
        akey_name = key_name_alias(key_name)
        if akey_name != None:
            key_name = akey_name
        return key_name

    def _get_sym_dict(self, symbol_name):
        search_default = False
        sub_id = symbol_name.find(NAME_START)
        if sub_id == -1:
            search_default = True
            main_name = symbol_name
        else:
            main_name = symbol_name[:sub_id]
            sub_name = symbol_name[sub_id + 1:-1]

        if search_default:
            if self.default_symbols_dict.has_key(main_name):
                sym_dict = self.default_symbols_dict[main_name]
            else:
                sym_dict = self.symbols_dict[main_name + "(basic)"]
        else:
            sname = main_name + NAME_START + sub_name + NAME_END
            try:
                sym_dict = self.symbols_dict[sname]
            except:
                for subdir in self.symbol_subdirs:
                    new_sname = subdir + "/" + sname
                    try:
                        sym_dict = self.symbols_dict[new_sname]
                        self.symbols_dict[sname] = sym_dict
                        break
                    except:
                        pass
                    
                if sym_dict == None:
                    sym_dict = self.default_symbols_dict[main_name]

        return sym_dict

    def _get_key_name(self, sym_dict, keysym, state):
        for dict_label, list_label in self.search_order_list:
            candidate_dict = sym_dict.get_dict(dict_label)
            for key_name in candidate_dict.keys():
                # workaround for sun_vndr/us keyboard
                # 'greater' or 'less' keys match LSGT wongly
                if key_name == "<LSGT>":
                    continue 
                key_values = candidate_dict[key_name]
                # group and level should be used here. (probably...)
                for i in range(len(key_values)):
                    if keysym in key_values[i]:
                        return key_name
                    else:
                        akeysym = keysym_alias(keysym)
                        if akeysym != None:
                            if akeysym in key_values[i]:
                                return key_name
            candidate_list = sym_dict.get_list(list_label)
            for l in candidate_list:
                sd = self._get_sym_dict(l)
                kn = self._get_key_name(sd, keysym, state)
                if kn != None:
                    return kn
                    
        return None

    def get_trans_ustr(self, symbol_name, key_name, state):
        keysym = self.get_keysym(symbol_name, key_name, state)
        if keysym == None:
            return None
        elif keysym.startswith("0x"):
            # This means keysym is likely to represent UCS-4 code string.
            code = int(keysym[2:], 16)
            if code > 0xffff:
                return ucs4_to_utf8(code)
        elif not keysym_to_unicode.has_key(keysym):
            # check if the representation is "UXXXX" form
            code = check_unicode_representation(keysym)
            if code == None:
                return None
        else:
            code = keysym_to_unicode[keysym]
            
        if state & ST_CAPS:
            if state & ST_LEVEL_2:
                code = unicode_lower(code)
            else:
                code = unicode_upper(code)

        return unichr(code).encode("utf-8")

    def _get_sym_array(self, cand_dict, key_name):
        if cand_dict.has_key(key_name):
            return cand_dict[key_name]
        akey_name = key_name_alias_r(key_name)
        if akey_name != None and cand_dict.has_key(akey_name):
            return cand_dict[akey_name]
        return None

    def get_keysym(self, symbol_name, key_name, state):

        if not self.symbols_dict.has_key(symbol_name):
            if not self.default_symbols_dict.has_key(symbol_name):
                raise SymbolsException("No such symbols name in DB : " + symbol_name)
            entry_symbol = self.default_symbols_dict[symbol_name]
        else:
            entry_symbol = self.symbols_dict[symbol_name]

        for dict_label, list_label in self.search_order_list:
            candidate_dict = entry_symbol.get_dict(dict_label)
            sym_array = self._get_sym_array(candidate_dict, key_name)
            if sym_array != None:
                sym = self._calc_sym(sym_array, state)
                if sym != "NoSymbol":
                    return sym
            candidate_list = entry_symbol.get_list(list_label)
            for l in candidate_list:
                s = self.get_keysym(l, key_name, state)
                if s != None:
                    return s

        return None

    def _calc_sym(self, sym_array, state):
        # sym_array is a array of keysym array
        # ie: [ [ a, b, c, d], [e, f, g, h]... ]
        # this method calculate symbols considering
        # state (ST_LEVEL_2, ST_LEVEL_3, ST_CAPS)
        num_grp = len(sym_array)
        if num_grp < 1:
            return None

        group = 0
        level = 0
        if state & ST_LEVEL_2:
            level += 1
        if state & ST_LEVEL_3:
            if num_grp < 2:
                level += 2
            else:
                group += 1

        grp_array = sym_array[group]
        # [[a, b, c, d], [e, f, g, h]...]
        # if c is None, then fallback to a
        # if d is None, then fallback to b
        # ...
        # if e is None, then fallback to a
        # if f is None, then fallback to e
        # if g is None, then fallback to e
        # if h is None, then fallback to f
        
        if group > len(sym_array):
            group = 0
        grp_array = sym_array[group]
        if level > len(grp_array):
            if level < 2:
                level = 0
            level -= 2

        symbol = grp_array[level]

        return symbol
    
    def get_symbols_dict(self):
        return self.symbols_dict

    def get_keycodes_dict(self):
        return self.keycodes_dict

    def get_types_dict(self):
        return self.types_dict
    
    def get_geometry_dict(self):
        return self.geometry_dict

    def get_keymap_dict(self):
        return self.keymap_dict

def xkbc_get_db():
    xkbc = XKBCDB(type = TYPE_SYMBOLS)
    return xkbc

if __name__ == "__main__":
    import cPickle as pickle

    try:
        print "Start parsing..."
        try:
            raise "x"
            f = open("_PICKLE_XKBC.dat")
            xkbc = pickle.load(f)
            f.close()
        except:
            xkbc = xkbc_get_db()
            f = open("_PICKLE_XKBC.dat", "w")
            pickle.dump(xkbc, f, 2)
            f.close()

        print "Finish parsing."
    except ParserException, ex:
        print ex
        sys.exit(1)
    except IndexError, iex:
        print "Index Error. Parser needs to be updated."
        sys.exit(1)

    print " Symbols # : ", len(xkbc.get_symbols_dict().keys())
    #print " Keycoes # : ", len(xkbc.get_keycodes_dict().keys())
    #print "   Tyeps # : ", len(xkbc.get_types_dict().keys())
    #print "  Keymap # : ", len(xkbc.get_keymap_dict().keys())
    #print "Geometry # : ", len(xkbc.get_geometry_dict().keys())

    print " ru + <AD02>, 0, 0 = ", xkbc.get_keysym("us(type6)", "<AD02>", 0)
    print " key_name for 'Cyrillic_yu' in 'ru' layout is " + str(xkbc.search_key_name('ru', 'Cyrillic_yu', 0))
    
