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

from constants import *
from parser import *

class KeycodesParser(Parser):

    def __init__(self, basedir):
        Parser.__init__(self, basedir)

    def get_component_class(self):
        return XKB_Keycodes

    def get_component_keyword(self):
        return KWD_KEYCODES

    def get_component_dirname(self):
        return DN_KEYCODES

from xkb_component import XKB_Component

class XKB_Keycodes(XKB_Component):
    #### xkb_keycodes data body ####
    _munimum = 0
    _maximum = 0
    _alias_dict = {}
    _alternate_dict = {}
    _indicator_dict = {}
    _virtual_indicator_dict = {}
    _symbol_code_dict = {}
    _include_list = []
    _augment_list = []
    ################################

    def __init__(self):
        XKB_Component.__init__(self)

    def set_content(self, content):
        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1

            if token == KWD_MINIMUM:
                self._minimum = int(content[i + 1]); i += 2 # skip "="
            elif token == KWD_MAXIMUM:
                self._maximum = int(content[i + 1]); i += 2 # skip "="
            elif token == KWD_ALIAS:
                self._alias_dict[content[i]] = content[i + 2]; i += 3
            elif token == KWD_ALTERNATE:
                self._alternate_dict[content[i]] = content[i + 2]; i += 3
            elif token == KWD_INDICATOR:
                self._indicator_dict[int(content[i])] = content[i + 2]; i += 3
            elif token == KWD_VIRTUAL:
                self._virtual_indicator_dict[int(content[i + 1])] = content[i + 3]; i += 4
            elif token == KWD_INCLUDE:
                self._include_list.append(content[i]); i += 1
            elif token == KWD_AUGMENT:
                self._augment_list.append(content[i]); i += 1
            elif token.startswith(SYM_START):
                self._symbol_code_dict[token] = content[i + 1]; i += 2
            elif token == LINE_END:
                pass
            else:
                print "Keycodes : Parser error: ", self._name, " : ", token

