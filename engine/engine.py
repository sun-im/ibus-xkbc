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

import gettext
import os
from os import path

import sys
sys.path.append(os.getenv('XKBC_SETUPDIR'))
from prefs import *
from vars import *
from layout import *
from keyeventutil import *

import gobject
import ibus
from ibus import keysyms
from ibus import modifier

from compose_tbl import *

_ = lambda a : gettext.dgettext("ibus-xkbc", a)

COMPOSE_END = 0
COMPOSE_START = 1
COMPOSE_PROCESS = 2

class Engine(ibus.EngineBase):

    # pickle data for symbols and rules
    __xkbc = None
    all_layouts = None

    def __init__(self, bus, object_path):
        super(Engine, self).__init__(bus, object_path)

        gettext.bindtextdomain("ibus-xkbc", os.getenv('XKBC_LOCALE_DIR'))
        gettext.bind_textdomain_codeset("ibus-xkbc", "UTF-8")

        self.__prop_dict = {}
        self.__config = Config(bus)
        self.__compose_state = COMPOSE_END
        self.__compose_dict = None

        self.__xkbc = prefs_get_xkbc_db()
        self.__prop_list = self._init_props()

        self.__target_layout_name = prefs_get_last_layout()
        self.__target_layout_id = self.__user_layouts.index(self.__target_layout_name)

    def __reset(self):
        pass

    # class variable
    __user_layouts = DEFAULT_LAYOUTS
    __conf = None
    __target_layout_id = 0
    __target_layout_name = "X"

    def _init_props(self):
        xkbc_props = ibus.PropList()

        layout_switch_prop = ibus.Property(key=u"LayoutSwitch",
                                           type=ibus.PROP_TYPE_MENU,
                                           label=self.__target_layout_name.capitalize(),
                                           tooltip=u"Layout Switch")
        self.__prop_dict[u"LayoutSwitch"] = layout_switch_prop

        props = ibus.PropList()
        selected = layout_make_object_list(self.__user_layouts)
        id = 0
        self.__layout_menu_items = []
        for lo in selected:
            props.append(ibus.Property(key=CMD_LAYOUT_SWITCH + str(id),
                                       type=ibus.PROP_TYPE_RADIO,
                                       label=lo.get_desc()))
            self.__layout_menu_items.append(lo.get_name())
            id += 1
                         
        props[self.__target_layout_id].set_state(ibus.PROP_STATE_CHECKED)
        for prop in props:
            self.__prop_dict[prop.key] = prop

        layout_switch_prop.set_sub_props(props)
        xkbc_props.append(layout_switch_prop)

        xkbc_props.append(ibus.Property(key=CMD_SETUP, tooltip=UI_TOOLTIP_SETUP))

        return xkbc_props

    def _refresh_prop_list(self):
        self.__prop_list = self._init_props()

    def _check_hotkeys(self, keyval, state):
        if self.__cycle_hotkeys != None:
            for hk in self.__cycle_hotkeys:
                if match_key(keyval, state, hk):
                    self._switch_to_next_layout()
                    return True

        if self.__rcycle_hotkeys != None:
            for hk in self.__rcycle_hotkeys:
                if match_key(keyval, state, hk):
                    self._switch_to_prev_layout()
                    return True

        if self.__compose_triggers != None:
            for hk in self.__compose_triggers:
                if match_key(keyval, state, hk):
                    self._compose_start()
                    return True

        return False

    def _switch_to_next_layout(self):
        num_of_layouts = len(self.__layout_menu_items)
        if (self.__target_layout_id + 1) >= num_of_layouts:
            self.__target_layout_id = 0
        else:
            self.__target_layout_id += 1
        self.__target_layout_name = self.__layout_menu_items[self.__target_layout_id]
        prefs_set_last_layout(self.__target_layout_name)
        self._refresh_prop_list()
        self.register_properties(self.__prop_list)

    def _switch_to_prev_layout(self):
        num_of_layouts = len(self.__layout_menu_items)
        if self.__target_layout_id == 0:
            self.__target_layout_id = num_of_layouts - 1
        else:
            self.__target_layout_id -= 1
        self.__target_layout_name = self.__layout_menu_items[self.__target_layout_id]
        prefs_set_last_layout(self.__target_layout_name)
        self._refresh_prop_list()
        self.register_properties(self.__prop_list)

    def _compose_get_cand_dict(self, keyval):
        if compose_dict.has_key(keyval):
            return compose_dict[keyval] # compose_dict comes from compose_tbl module
        return None

    def _compose_start(self):
        self.__compose_state = COMPOSE_START

    def _compose_end(self):
        self.__compose_state = COMPOSE_END
        self.__compose_dict = None

    def _compose_process(self, dict):
        self.__compose_state = COMPOSE_PROCESS
        self.__compose_dict = dict

    def _compose_get_char(self, val):
        if self.__compose_dict.has_key(val):
            return self.__compose_dict[val]
        return val

    def _compose_state(self):
        return self.__compose_state

    if ibus.get_version() >= '1.2.0':
        def process_key_event(self, keyval, keycode, state):
            return self._process_key_event_internal(keyval, keycode, state)
    else:
        def process_key_event(self, keyval, state):
            return self._process_key_event_internal(keyval, 0, state)

    def _process_key_event_internal(self, keyval, keycode, state):
        is_press = (state & modifier.RELEASE_MASK) == 0

        if not is_press:
            return False

        self.__cycle_hotkeys = prefs_get_cycle_hotkeys()
        self.__rcycle_hotkeys = prefs_get_rcycle_hotkeys()
        self.__compose_triggers = prefs_get_compose_triggers()

        if self._check_hotkeys(keyval, state):
            return True

        # after checking hotkeys, non character keys are passed though
        if (state & ST_CONTROL) or (state & ST_ALT_L) or non_trans_key(keyval):
            return False

        self.__source_layout_name = prefs_get_physical_layout()

        keysym = keysyms.keycode_to_name(keyval)
        key_name = self.__xkbc.search_key_name(self.__source_layout_name, keysym, state)
        commit_str = self.__xkbc.get_trans_ustr(self.__target_layout_name, key_name, state)

        if commit_str == None:
            return False
        
        if self._compose_state() == COMPOSE_START:
            cd = self._compose_get_cand_dict(commit_str)
            if cd != None:
                self._compose_process(cd)
                return True
            else:
                self._compose_end()
        elif self._compose_state() == COMPOSE_PROCESS:
            commit_str = self._compose_get_char(commit_str)
            self._compose_end()

        self.__commit_string(commit_str)
        return True

    def page_up(self):
        return False

    def page_down(self):
        return False

    def cursor_up(self):
        return False

    def cursor_down(self):
        return False

    def __commit_string(self, text):
        self.commit_text(ibus.Text(text))

    def focus_in(self):
        self._refresh_prop_list()
        self.register_properties(self.__prop_list)
        pass

    def focus_out(self):
        pass

    def reset(self):
        pass

    def property_activate(self, prop_name, state):
        if prop_name == CMD_SETUP:
            self._start_setup()
        elif prop_name.startswith(CMD_LAYOUT_SWITCH):
            id = int(prop_name.split(CMD_LAYOUT_SWITCH)[1])
            layout_name = self.__layout_menu_items[id]
            self.__target_layout_name = layout_name
            self.__target_layout_id = id
            self._refresh_prop_list()
            prefs_set_last_layout(layout_name)
            self.register_properties(self.__prop_list)

    __setup_pid = 0

    def _start_setup(self):
        if Engine.__setup_pid != 0:
            pkd, state = os.waitpid(Engine.__setup_pid, os.P_NOWAIT)
            if pid != Engine.__setup_pid:
                return
            Engine.__setup_pid = 0
        if os.getenv('LIBEXECDIR') == None:
            return
        setup_cmd = path.join(os.getenv('LIBEXECDIR'), "ibus-setup-xkbc")
        Engine.__setup_id = os.spawnl(os.P_NOWAIT, setup_cmd, "ibus-setup-xkbc")

    @classmethod
    def CONFIG_RELOADED(cls, bus):
        if not cls.__conf:
            cls.__conf = Config(bus)

        l = cls.__conf.get_user_layouts()
	if l != None and len(l) > 0:
            cls.__user_layouts = l
        cls.__target_layout_name = cls.__user_layouts[0]
        
    @classmethod
    def CONFIG_VALUE_CHANGED(cls, bus, section, name, value):
        if section == KEY_ROOT and name == KEY_USER_LAYOUT:
            cls.__user_layouts = value

class Config:
    def __init__(self, bus):
        self.conf = bus.get_config() if bus else ibus.Bus().get_config()

    def get_user_layouts(self):
        l = self.conf.get_value(KEY_ROOT, KEY_USER_LAYOUT, None)
        return l
    
