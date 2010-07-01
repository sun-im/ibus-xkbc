# vim:set et sts=4 sw=4:
#
# ibus-xkbc - The Input Bus Keyboard Layout emulaton engine.
#
# Copyright (c) 2009, 2010 Oracle and/or its affiliates. All rights reserved.
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

from constants import *
from parser import *

class SymbolsParser(Parser):

    def __init__(self, basedir):
        Parser.__init__(self, basedir)

    def get_component_class(self):
        return XKB_Symbols

    def get_component_keyword(self):
        return KWD_SYMBOLS

    def get_component_dirname(self):
        return DN_SYMBOLS

from xkb_component import XKB_Component

class XKB_Symbols(XKB_Component):

    def __init__(self):
        XKB_Component.__init__(self)
        self._key_dict = {}
        self._include_list = []
        self._override_key_dict = {}
        self._override_list = []
        self._replace_key_dict = {}
        self._replace_list = []
        self._augment_key_dict = {}
        self._augment_list = []
        self._name_dict = {}
        self._key_type_dict = {}
        self._modifier_dict = {}
        self._virtual_modifier_list = []

    def get_dict(self, label):
        if label == MAIN_DICT:
            return self._key_dict
        if label == OVERRIDE_DICT:
            return self._override_key_dict
        if label == AUGMENT_DICT:
            return self._augment_key_dict
        if label == REPLACE_DICT:
            return self._replace_key_dict

    def get_list(self, label):
        if label == INCLUDE_LIST:
            return self._include_list
        if label == OVERRIDE_LIST:
            return self._override_list
        if label == AUGMENT_LIST:
            return self._augment_list
        if label == REPLACE_LIST:
            return self._replace_list

    def set_content(self, content):
        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1

            if token in KWD_KEY:
                key_name = content[i]; i += 1
                self._key_dict[key_name] = self._make_symbols(content[i]); i += 1
            elif token == KWD_INCLUDE:
                self._include_list.append(content[i]); i += 1
            elif token == KWD_OVERRIDE:
                if content[i] in KWD_KEY:
                    key_name = content[i + 1]; i += 2 # skip 'key'
                    self._override_key_dict[key_name] = self._make_symbols(content[i]); i += 1
                else:
                    self._override_list.append(content[i]); i += 1
            elif token == KWD_REPLACE:
                if content[i] in KWD_KEY:
                    key_name = content[i + 1]; i += 2 # skip 'key'
                    self._replace_key_dict[key_name] = self._make_symbols(content[i]); i += 1
                else:
                    self._replace_list.append(content[i]); i += 1
            elif token == KWD_AUGMENT:
                if content[i] in KWD_KEY:
                    key_name = content[i + 1]; i += 2 # skip 'key'
                    self._augment_key_dict[key_name] = self._make_symbols(content[i]); i += 1
                else:
                    self._augment_list.append(content[i]); i += 1
            elif token == KWD_NAME:
                gname = content[i + 1]; i += 3 # skip '[' and ']'
                self._name_dict[gname] = content[i + 1]; i += 2 # skip '='
            elif token == KWD_MODIFIER_MAP:
                mod_name = content[i];
                mod_list = content[i + 1]; i += 2
                self._modifier_dict[mod_name] = mod_list
            elif token == KWD_KEY_TYPE:
                if content[i] == '=':
                    gname = NONGROUP_NAME
                else:
                    gname = content[i + 1]; i += 3 # skip '[' and ']'
                self._key_type_dict[gname] = content[i + 1]; i += 2 # skip '='
            elif token == KWD_VIRTUAL_MODIFIERS:
                t = content[i]
                while t != LINE_END:
                    self._virtual_modifier_list.append(t)
                    i += 1; t = content[i]
            elif token == LINE_END:
                pass # just ignoe, LINE_END is mianingfull in case of KWD_VIRTUAL_MODIFIER
            else:
                raise ParserException("Symbols contents: Parse error: " + self._name +  " : " + token)

    # private utilities
    def _make_symbols(self, tokens):
        key_value = _KeyValue()
        length = len(tokens)
        i = 0
        while i < length:
            token = tokens[i]; i += 1
            if token == KWD_TYPE:
                type_key = tokens[i + 1]
                type_value = tokens[i + 4]; i += 5
                key_value.set_type(type_key, type_value)
            if token == LIST_START:
                sym_list = []
                while tokens[i] <> LIST_END:
                    sym_list.append(tokens[i]); i += 1
                key_value.add_sym_list(sym_list)
                i += 1
        return key_value

class _KeyValue:
    def __init__(self):
        self._type_map = {}
        self._symbol_array = []

    def __getitem__(self, index):
        return self._symbol_array[index]

    def __len__(self):
        return len(self._symbol_array)
    
    def set_type(self, key, value):
        self._type_map[key] = value

    def add_sym_list(self, sym_list):
        self._symbol_array.append(sym_list)


class SymbolsException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
