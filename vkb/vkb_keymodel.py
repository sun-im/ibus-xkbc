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

import os
import sys

from ibus import keysyms

sys.path.append(os.getenv('XKBC_LIBDIR'))

from constants import *
from vkb_constants import *
from vkb_signal import *

messenger = Messenger()

class VKBKeyModel(object):
    def __init__(self, xkbc_db, symbol_name, key_name):
        self._type = None
        self._xkbc = xkbc_db
        self._symbol_name = symbol_name
        self._key_name = key_name

    def get_type(self):
        return self._type

    def lock_key(self):
        return False

    def change_state(self, vkb):
        pass

    # need to be overridden
    def get_display_label(self, state):
        return None

    # used for generating fake keyevent
    def get_keyvalue(self, state):
        keysym = self._xkbc.get_keysym(self._symbol_name, self._key_name, state)
        return keysyms.name_to_keycode(keysym)

    # need to be overridden
    def get_display_labels(self):
        return None

    # need to be overridden
    def clicked(self, state):
        pass

class VKBCharKeyModel(VKBKeyModel):
    def __init__(self, xkbc_db, symbol_name, key_name):
        VKBKeyModel.__init__(self, xkbc_db, symbol_name, key_name)
        self._type = VKB_CHAR_KEY

        # some layout has not definition for <SPCE> and procudes None
        if key_name == "<SPCE>":
            self._labels = [[" ", " ", " ", " "]]
        else:
            self._labels = None

    def get_display_label(self, state):
        if self._labels == None:
            self.get_display_labels()

        return self._get_label(state)

    def get_display_labels(self):
        if self._labels == None:
            self._labels = self._xkbc.get_unichar_array(self._symbol_name, self._key_name)

        return self._labels

    def _get_label(self, state):
        # self._labels : [[x, x, x, x], [X, X, X, X]]
        # second list has capitalized character list if any
        #
        labels = self._labels

        if state & ST_SHIFT and state & ST_LEVEL_3:
            if state & ST_CAPS and len(labels) > 1:
                return labels[1][3]
            else:
                return labels[0][3]
        if state & ST_SHIFT:
            if state & ST_CAPS and len(labels) > 1:
                return labels[1][1]
            else:
                return labels[0][1]
        if state & ST_LEVEL_3:
            if state & ST_CAPS and len(labels) > 1:
                return labels[1][2]
            else:
                return labels[0][2]

        if state & ST_CAPS and len(labels) > 1:
            return labels[1][0]
        else:
            return labels[0][0]

        return self._labels[0][0]

    def clicked(self, state):
        if state & ST_CONTROL:
            ctrl_val = self.get_keyvalue(state)
            messenger.send_key(ctrl_val, state)
        else:
            l = self._get_label(state)
            messenger.send_text(l)

class VKBKeypadKeyModel(VKBCharKeyModel):
    def __init__(self, xkbc_db, symbol_name, key_name):
        VKBCharKeyModel.__init__(self, xkbc_db, symbol_name, key_name)
        self._type = VKB_KEYPAD_KEY
        self._symbol_name = "keypad(x11)"

    def _get_label(self, state):
        # Keypad label is static for now
        labels = keypad_key_names[self._key_name]
        if state & ST_NUM_LOCK and len(labels) > 1:
            return labels[1]
        
        return labels[0]

    def clicked(self, state):
        if state & ST_NUM_LOCK:
            state |= ST_SHIFT
        v = self.get_keyvalue(state)
        print "KeyPad:"
        messenger.send_key(v, state)

class VKBNonCharKeyModel(VKBKeyModel):
    def __init__(self, xkbc_db, symbol_name, key_name):
        VKBKeyModel.__init__(self, xkbc_db, symbol_name, key_name)

    def get_display_labels(self):
        return [[self.get_display_label(0)]]

class VKBFuntionKeyModel(VKBNonCharKeyModel):
    def __init__(self, xkbc_db, symbol_name, key_name):
        VKBNonCharKeyModel.__init__(self, xkbc_db, symbol_name, key_name)
        self._type = VKB_FUNC_KEY
        self._symbol_name = "pc(function)"

    def get_display_label(self, state):
        return function_key_names[self._key_name]

    def clicked(self, state):
        v = self.get_keyvalue(state)
        messenger.send_key(v, state)

class VKBModifierKeyModel(VKBNonCharKeyModel):
    def __init__(self, xkbc_db, symbol_name, key_name):
        VKBNonCharKeyModel.__init__(self, xkbc_db, symbol_name, key_name)
        self._type = VKB_MODIFIER_KEY
        if modifier_state_change_dict.has_key(self._key_name):
            self._change_state = True
        else:
            self._change_state = False

    def lock_key(self):
        return True

    def change_state(self, vkb):
        if self._change_state:
            vkb.set_state(modifier_state_change_dict[self._key_name])

    def get_display_label(self, state):
        return modifier_key_names[self._key_name]

class VKBControlKeyModel(VKBKeyModel):
    def __init__(self, xkbc_db, symbol_name, key_name):
        VKBKeyModel.__init__(self, xkbc_db, symbol_name, key_name)
        self._type = VKB_CONTROL_KEY
        self._symbol_name = "pc(pc105)"

    def get_display_label(self, state):
        return control_key_names[self._key_name]

    def clicked(self, state):
        v = self.get_keyvalue(state)
        messenger.send_key(v, state)


# Factory function for VKBKeyModel
def vkb_keymodel_get_key_model(xkbc_db, symbol_name, key_name):
    if function_key_names.has_key(key_name):
        model = VKBFuntionKeyModel(xkbc_db, symbol_name, key_name)
    elif modifier_key_names.has_key(key_name):
        model = VKBModifierKeyModel(xkbc_db, symbol_name, key_name)
    elif control_key_names.has_key(key_name):
        model = VKBControlKeyModel(xkbc_db, symbol_name, key_name)
    elif keypad_key_names.has_key(key_name):
        model = VKBKeypadKeyModel(xkbc_db, symbol_name, key_name)
    else:
        model = VKBCharKeyModel(xkbc_db, symbol_name, key_name)

    return model

function_key_names = {
    "<FK01>": "F1",
    "<FK02>": "F2",
    "<FK03>": "F3",
    "<FK04>": "F4",
    "<FK05>": "F5",
    "<FK06>": "F6",
    "<FK07>": "F7",
    "<FK08>": "F8",
    "<FK09>": "F9",
    "<FK10>": "F10",
    "<FK11>": "F11",
    "<FK12>": "F12",
    "<FK13>": "F13",
    "<PRSC>": "Print Sc",
    "<SCLK>": "Scroll Lock",
    "<PAUS>": "Pause",
    "<INS>": "Insert",
    "<HOME>": "Home",
    "<PGUP>": "Page Up",
    "<END>": "End",
    "<PGDN>": "Page Down",
    "<UP>": "Up",
    "<LEFT>": "Left",
    "<DOWN>": "Down",
    "<RGHT>": "Right",
    "<STOP>": "Stop",
    "<AGAI>": "Again",
    "<PROP>": "Props",
    "<UNDO>": "Undo",
    "<FRNT>": "Front",
    "<COPY>": "Copy",
    "<OPEN>": "Open",
    "<PAST>": "Paste",
    "<FIND>": "Find",
    "<CUT>": "Cut",
    "<HELP>": "Help",
    "<COMP>": "Comp",
    "<HZTG>": "Henkan",
    "<HENK>": "Mode",
    "<MENU>": "Menu",
    }

modifier_key_names = {
    "<LFSH>" : "Shift",
    "<LCTL>" : "Control",
    "<RTSH>" : "Shift",
    "<RCTL>" : "Ctrl",
    "<LALT>" : "Alt",
    "<RMTA>" : "Meta",
    "<LMTA>" : "Meta",
    "<LWIN>" : "Win",
    "<RWIN>" : "Win",
    "<CAPS>" : "Caps Lock",
    "<ALGR>" : "AltG",
    "<RALT>" : "Alt_R",
    "<NMLK>" : "Num Lock",
    }

control_key_names = {
    "<BKSP>" : "Back Space",
    "<TAB>" : "Tab",
    "<RTRN>" : "Return",
    "<DELE>" : "Del",
    "<ESC>" : "Esc",
    "<KPEN>" : "Enter",
    }    

keypad_key_names = {
    "<KPDV>" : ("/"),
    "<KPMU>" : ("*"),
    "<KPSU>" : ("-"),
    "<KPAD>" : ("+"),
    "<KPDL>" : ("Del", "."),
    "<KP1>" : ("End", "1"),
    "<KP2>" : ("Down", "2"),
    "<KP3>" : ("Pg Dn", "3"),
    "<KP4>" : ("Left", "4"),
    "<KP5>" : ("", "5"),
    "<KP6>" : ("Right", "6"),
    "<KP7>" : ("Home", "7"),
    "<KP8>" : ("Up", "8"),
    "<KP9>" : ("Pg Up", "9"),
    "<KP0>" : ("Ins", "0"),
    }    

modifier_state_change_dict = {
    "<ALGR>" : ST_LEVEL_3,
    "<LFSH>" : ST_SHIFT,
    "<RTSH>" : ST_SHIFT,
    "<CAPS>" : ST_CAPS,
    "<RALT>" : ST_LEVEL_3,
    "<NMLK>" : ST_NUM_LOCK,
    "<LCTL>" : ST_CONTROL,
    "<RCTL>" : ST_CONTROL,
    "<RALT>" : ST_ALT_R,
    "<LALT>" : ST_ALT_L
    }

