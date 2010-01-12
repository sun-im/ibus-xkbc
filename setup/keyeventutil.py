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

from ibus import keysyms

# temp (use ibus/modifer)
ST_SHIFT = 1 << 0
ST_CONTROL = 1 << 2
ST_ALT_L = 0x4000048

def match_key(keyval, keystate, tgt_key_str):
    code, state = string_to_event(tgt_key_str)
    
    if keyval == code and keystate == state:
        return True
    return False

def event_to_string(keyval, state):
    mod = None

    if state & ST_SHIFT:
        mod = "Shift"
    if state & ST_CONTROL:
        if mod == None:
            mod = "Control"
        else:
            mod += "+Control"
    if state & ST_ALT_L:
        if mod == None:
            mod = "Alt_L"
        else:
            mod += "+Alt_L"

    name = keysyms.keycode_to_name(keyval)
    if mod == None:
        return name
    else:
        return mod + "+" + name

    
def string_to_event(s):
    state = 0
    code = 0
    num_mod = 0
    l = s.split("+")
    for t in l:
        if t.startswith("Shift"):
            state |= ST_SHIFT
        elif t.startswith("Control"):
            state |= ST_CONTROL
        elif t.startswith("Alt_L"):
            state |= ST_ALT_L
        else:
            code = keysyms.name_to_keycode(t)
            
    return code, state

