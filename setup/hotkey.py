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

import gtk

import os
import sys
sys.path.append(os.getenv('XKBC_LIBDIR'))

from ibus import keysyms
from prefs import *
from keyeventutil import *

class CycleHotkeyList(object):

    def __init__(self, p):
        self.parent = p
        self.label_string = UI_CYCLE_KEY
        self._hotkeys = CycleHotkeys()
        self._setup_model(self._hotkeys)
        self._setup_window(self.model)
        self.add_dialog = None

    def _setup_model(self, hotkeys):
        self.model = gtk.ListStore(str)
        hkl = hotkeys.get_keys()
        for key in hotkeys:
            self.model.append([`key`])

    def _setup_window(self, model):
        self.vbox = gtk.VBox(False, 10)
        self.hbox = gtk.HBox(False, 10)

        self.view = gtk.TreeView(model)
        column = gtk.TreeViewColumn(UI_KEYS)
        self.view.append_column(column)
        self.view.set_headers_visible(False)
        text_renderer = gtk.CellRendererText()
        column.pack_start(text_renderer, True)
        column.add_attribute(text_renderer, 'text', 0)

        self.sw = gtk.ScrolledWindow()
        self.sw.add_with_viewport(self.view)

        self.button_box = gtk.VBox(False, 10)
        self.add_button = gtk.Button(UI_ADD)
        self.add_button.connect("clicked", self.add_key, None)
        self.del_button = gtk.Button(UI_DEL)
        self.del_button.connect("clicked", self.del_key, None)
        self.button_box.pack_start(self.add_button, False, False, 20)
        self.button_box.pack_start(self.del_button, False, False, 20)

        self.hbox.pack_start(self.sw, True, True, 10)
        self.hbox.pack_start(self.button_box, False, False, 20)

        self.vbox.pack_start(gtk.Label(self.label_string), False, False, 0)
        self.vbox.pack_start(self.hbox, True, True, 0)

    def del_key_from_model(self, keystr):
        self.model.remove(keystr)

    def add_key(self, widget, data=None):
        if self.add_dialog == None:
            self.add_dialog = AddKeyDialog(self.parent, self.model)

        self.add_dialog.show()

    def del_key(self, widget, data=None):
        cursor = self.view.get_cursor()
        if cursor == None or cursor[0] == None:
            return

        self.model.remove(self.model.get_iter(cursor[0]))
    
    def save_hotkey(self, widget, event, data=None):
        l = []
        itr = self.model.get_iter_first()
        while itr:
            l.append(self.model.get_value(itr, 0))
            itr = self.model.iter_next(itr)

        prefs_set_cycle_hotkeys(l)
        
    def get_model(self):
        return self.model

    def get_window(self):
        return self.vbox
    
class RCycleHotkeyList(CycleHotkeyList):

    def __init__(self, p):
        self.parent = p
        self.label_string = UI_RCYCLE_KEY
        self._hotkeys = RCycleHotkeys()
        self._setup_model(self._hotkeys)
        self._setup_window(self.model)
        self.add_dialog = None

    def save_hotkey(self, widget, event, data=None):
        l = []
        itr = self.model.get_iter_first()
        while itr:
            l.append(self.model.get_value(itr, 0))
            itr = self.model.iter_next(itr)

        prefs_set_rcycle_hotkeys(l)

DELIMITER = ","

class CycleHotkeys(object):
    def __init__(self):
        self._hotkeys_str_list = prefs_get_cycle_hotkeys()
        self._hotkeys = []	# list of class Key instance
        self._init_hotkeys()

    def _init_hotkeys(self):
        for s in self._hotkeys_str_list:
            code, state = string_to_event(s)
            self._hotkeys.append(Key(code, state))

    def __getitem__(self, index):
        return self._hotkeys[index]

    def get_keys(self):
        return self._hotkeys

    def match(self, key):
        return key in self._hotkeys

    def add_key(self, key):
        self._hotkeys.append(key)

    def del_key(self, key):
        self._hotkeys.remove(key)

class RCycleHotkeys(CycleHotkeys):
    def __init__(self):
        self._hotkeys_str_list = prefs_get_rcycle_hotkeys()
        self._hotkeys = []
        self._init_hotkeys()
        

class Key(object):
    def __init__(self, keyval, state):
        self._keyval = keyval
        self._state = state
        self._strval = event_to_string(keyval, state)

    def __repr__(self):
        return self._strval

class AddKeyDialog(object):
    def __init__(self, p, model):
        self.model = model

        add_button = gtk.Button(UI_ADD2)
        add_button.connect("clicked", self.add_hotkey, None)

        cancel_button = gtk.Button(UI_CANCEL)
        cancel_button.connect("clicked", self.close_dialog, None)
        
        type_label = gtk.Label("<i>" + UI_TYPEMSG + "</i>")
        type_label.set_use_markup(True)
        event_box = gtk.EventBox()
        event_box.add(type_label)
        event_box.add_events(gtk.gdk.KEY_PRESS)
        event_box.set_flags(gtk.CAN_FOCUS)
        event_box.connect("key_press_event", self.show_type_key, None)
        event_box.set_size_request(200, 100)

        frame = gtk.Frame()
        frame.add(event_box)

        self.show_label = gtk.Label("")
        self.show_label.set_size_request(200, 30)
        self.show_label.set_use_markup(True)

        f = gtk.DIALOG_DESTROY_WITH_PARENT
        self.dialog = gtk.Dialog(UI_ADD_DIALOG_TITLE, parent=p, flags = f)
        self.dialog.connect("delete_event", lambda w, e: self.close_dialog(None, None))
        self.dialog.action_area.pack_start(add_button, True, False, 50)
        self.dialog.action_area.pack_start(cancel_button, True, False, 50)
        self.dialog.vbox.pack_start(frame, True, True, 0)
        self.dialog.vbox.pack_start(self.show_label, True, True, 0)

    def add_hotkey(self, widget, event, data=None):
        if len(self.cur_keystr) > 0:
            self.model.append([self.cur_keystr])
        self.dialog.hide_all()

    def close_dialog(self, event, data=None):
        self.dialog.hide_all()

    def show(self):
        self.hotkey = None
        self.dialog.show_all()
        
    def show_type_key(self, widget, event, data=None):
        self.cur_keystr = event_to_string(event.keyval, event.state)
        s = "<b>" + self.cur_keystr + "</b>"
        self.show_label.set_label(s)
        self.hotkey = event

if __name__ == '__main__':
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("Hotkey pane test")
    window.set_size_request(400, 400)
    window.connect("delete_event", lambda w, e: gtk.main_quit())
    box = gtk.VBox(False, 0)
    keylist = CycleHotkeyList()
    rkeylist = RCycleHotkeyList()
    box.pack_start(keylist.get_window(), True, False, 20)
    box.pack_start(gtk.HSeparator())
    box.pack_start(rkeylist.get_window(), True, False, 20)

    window.add(box)
    window.show_all()
    gtk.main()

