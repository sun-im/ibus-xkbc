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

import ibus

import os
import sys

from vars import *

sys.path.append(os.getenv('XKBC_LIBDIR'))
from xkbc import *

import cPickle as pickle
PICKLE_FILE = os.getenv('XKBC_DATAFILE')
all_layouts = None
all_symbols = None

def prefs_get_symbols_data():
    global all_layouts, all_symbols
    if all_symbols == None:
        f = open(PICKLE_FILE)
        all_layouts, all_symbols = pickle.load(f)
        f.close()
    return all_symbols

def prefs_get_layouts():
    global all_layouts, all_symbols
    if all_layouts == None:
        f = open(PICKLE_FILE)
        all_layouts, all_symbols = pickle.load(f)
        f.close()
    return all_layouts
    
def recreate_db(fname):
    try:
        f = open(fname, "w")
    except:
        print "You seems to have no write permission to file : ", fname, "."
        sys.exit(1)
        
    layouts = xkbc_get_layouts()
    xkbcdb = xkbc_get_db()
    pickle.dump([layouts, xkbcdb], f, 2)
    f.close()

class Prefs(object):

    def __init__(self):
        self.default = {}
        self.modified = {}
        self.new = {}
        self.__physical_layout = None
        self.__cycle_hotkeys = None
        self.__rcycle_hotkeys = None

        self.__all_layout = None
        try:
            self.__config = ibus.Bus().get_config()
        except:
            # for standalone debug
            self.__config = _ConfigDummy()

        self.__user_layout = self.get_user_layouts_from_config()

    def get_config(self):
        return self.__config

    def get_user_layouts(self):
        return self.__user_layout

    def get_user_layouts_from_config(self):
        self.__user_layout = self.__config.get_value(KEY_ROOT, KEY_USER_LAYOUT, None)
        if self.__user_layout == None:
            self.__user_layout = DEFAULT_LAYOUTS
        return self.__user_layout

    def get_physical_layout(self):
        if self.__physical_layout != None:
            return self.__physical_layout
        
        physical_name = self.__config.get_value(KEY_ROOT, KEY_PHYSICAL_LAYOUT, None)
        if physical_name != None:
            return physical_name

        return DEFAULT_PHYSICAL_LAYOUT

    def get_all_layouts(self):
        if self.__all_layout == None:
            self.__all_layout = prefs_get_layouts()
        return self.__all_layout

    def save_user_layouts(self, name_list):
        self.__user_layout = name_list
        self.__config.set_value(KEY_ROOT, KEY_USER_LAYOUT, name_list)

    def save_physical_layout(self, name):
        self.__physical_layout = name
        self.__config.set_value(KEY_ROOT, KEY_PHYSICAL_LAYOUT, name)

    def get_cycle_hotkeys(self):
        if self.__cycle_hotkeys != None:
            return self.__cycle_hotkeys

        cycle_hotkeys = self.__config.get_value(KEY_ROOT, KEY_CYCLE_HOTKEY, None)
        if cycle_hotkeys != None:
            return cycle_hotkeys

        return DEFAULT_CYCLE_HOTKEY

    def get_rcycle_hotkeys(self):
        if self.__rcycle_hotkeys != None:
            return self.__rcycle_hotkeys

        rcycle_hotkeys = self.__config.get_value(KEY_ROOT, KEY_RCYCLE_HOTKEY, None)
        if rcycle_hotkeys != None:
            return rcycle_hotkeys

        return DEFAULT_RCYCLE_HOTKEY

    def get_compose_triggers(self):
        # compose keys are hardcoded now
        return DEFAULT_COMPOSE_TRIGGERS

    def save_cycle_hotkeys(self, hotkeys):
        # hotkeys is a list of hotkey string
        self.__cycle_hotkeys = hotkeys
        self.__config.set_value(KEY_ROOT, KEY_CYCLE_HOTKEY, hotkeys)

    def save_rcycle_hotkeys(self, hotkeys):
        # hoekeys is a list of hotkey string
        self.__rcycle_hotkeys = hotkeys
        self.__config.set_value(KEY_ROOT, KEY_RCYCLE_HOTKEY, hotkeys)

    def save_last_layout(self, layout_name):
        self.__config.set_value(KEY_ROOT, KEY_LAST_LAYOUT, layout_name)

    def get_last_layout(self):
        name = self.__config.get_value(KEY_ROOT, KEY_LAST_LAYOUT, None)
        if name != None and name in self.__user_layout:
            return name

        return DEFAULT_LAYOUTS[0]

class _ConfigDummy:
    def __init__(self):
        self.__dict = {}

    def get_value(self, section, key, d):
        try:
            return self.__dict[key]
        except:
            return d

    def set_value(self, section, key, value):
        pass

_prefs = Prefs()

# returns list of xkb_rules.Layout instance
# which has the 'selected' attribute
#
def prefs_get_all_layouts():
    all = _prefs.get_all_layouts()
    user = _prefs.get_user_layouts()
    for l in all.values():
        if l.get_name() in user:
            l.set_selected(True)
        for v in l.get_variants():
            if v.get_name() in user:
                v.set_selected(True)
    return all

# set name string list
def prefs_set_user_layouts_by_name(layouts):
    _prefs.save_user_layouts(layouts)

def prefs_set_physical_layout_by_name(layout):
    _prefs.save_physical_layout(layout)

def _get_layout_objects(name_list):
    all_layouts = _prefs.get_all_layouts()
    user_layout_obj = []
    for u in name_list:
        v = None
        p = u
        if u.find("(") != -1:
            p, v = u.split("(")
            v = v[:-1]
        try:
            layout = all_layouts[p]
            if v != None:
                for vobj in layout.get_variants():
                    if u == vobj.get_name():
                        user_layout_obj.append(vobj)
            else:
                user_layout_obj.append(layout)
        except:
            pass

    return user_layout_obj
    
# returns Layout object list
def prefs_get_user_layouts():
    user_list = _prefs.get_user_layouts()
    return _get_layout_objects(user_list)

def prefs_get_physical_layout():
    return _prefs.get_physical_layout()

def prefs_get_cycle_hotkeys():
    return _prefs.get_cycle_hotkeys()

def prefs_get_rcycle_hotkeys():
    return _prefs.get_rcycle_hotkeys()

def prefs_get_compose_triggers():
    return _prefs.get_compose_triggers()

def prefs_set_cycle_hotkeys(keys_list):
    _prefs.save_cycle_hotkeys(keys_list)

def prefs_set_rcycle_hotkeys(keys_list):
    _prefs.save_rcycle_hotkeys(keys_list)

def prefs_set_last_layout(layout_name):
    _prefs.save_last_layout(layout_name)

def prefs_get_last_layout():
    return _prefs.get_last_layout()

        
