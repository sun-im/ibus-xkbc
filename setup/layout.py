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
import gtk

from vars import *
from prefs import *

class TargetLayoutList(object):
    def __init__(self):
        self.model = gtk.TreeStore(str, str, 'gboolean') # name, desc, selected
        layouts = prefs_get_all_layouts()
        self.all_layouts = layouts
        layouts = layouts.values()
        layouts.sort()
        self.setup_model(layouts)

        self.view = gtk.TreeView(self.model)
        self.view.set_enable_search(True)
        self.view.set_headers_clickable(True)
        self.view.set_reorderable(True)

        self.layout_col = gtk.TreeViewColumn(UI_LAYOUT_COLUMN)
        self.view.append_column(self.layout_col)
        self.select_col = gtk.TreeViewColumn(UI_SELECT_COLUMN)
        self.view.append_column(self.select_col)

        self.text_renderer = gtk.CellRendererText()
        self.layout_col.pack_start(self.text_renderer, True)
        self.layout_col.add_attribute(self.text_renderer, 'text', 1)
        self.layout_col.set_sort_column_id(1)
        
        self.bool_renderer = gtk.CellRendererToggle()
        self.select_col.pack_start(self.bool_renderer, True)
        self.select_col.add_attribute(self.bool_renderer, "active", 2)
        self.bool_renderer.connect("toggled", self.toggle_cb, None)
        self.bool_renderer.set_property("activatable", True)

        self.expand_selected_row()

    def setup_model(self, layouts):
        for l in layouts:
            p = self.model.append(None, [l.get_name(), l.get_desc(), l.get_selected()])
            for v in l.get_variants():
                self.model.append(p, [v.get_name(), v.get_desc(), v.get_selected()])

    def get_view(self):
        return self.view

    def get_model(self):
        return self.model

    def save_layouts(self, widget, data):
        user_layout = []
        itr = self.model.get_iter_first()
        while itr:
            selected = self.model.get_value(itr, 2)
            if selected == True:
                user_layout.append(self.model.get_value(itr, 0))
            c_itr = self.model.iter_children(itr)
            while c_itr:
                selected_c = self.model.get_value(c_itr, 2)
                if selected_c == True:
                    user_layout.append(self.model.get_value(c_itr, 0))
                c_itr = self.model.iter_next(c_itr)
            itr = self.model.iter_next(itr)

        prefs_set_user_layouts_by_name(user_layout)

    def toggle_cb(self, cell, path, user_data):
        iter = self.model.get_iter(path)
        selected = self.model.get_value(iter, 2)
        self.model.set_value(iter, 2, not selected)

    def expand_selected_row(self):
        iter = self.model.get_iter_first()
        while iter:
            c_iter = self.model.iter_children(iter)
            while c_iter:
                checked = self.model.get_value(c_iter, 2)
                if checked:
                    path = self.model.get_path(iter)
                    self.view.expand_row(path, False)
                c_iter = self.model.iter_next(c_iter)
            iter = self.model.iter_next(iter)
        

class SourceLayoutList(TargetLayoutList):
    _source_id = None
    
    def __init__(self):
        super(SourceLayoutList, self).__init__()
        self._source_id = None

    def _get_source_layout_id(self):
        if self._source_id == None:
            self._source_id = prefs_get_physical_layout()
            
        return self._source_id

    def _set_source_layout_id(self, id):
        self._source_id = id

    # Override
    def setup_model(self, layouts):
        for l in layouts:
            p = self.model.append(None, [l.get_name(), l.get_desc(), False])
            for v in l.get_variants():
                self.model.append(p, [v.get_name(), v.get_desc(), False])

        self._set_select_layout(self._get_source_layout_id(), True)
                                      
    def _set_select_layout(self, id, b):
        iter = self.model.get_iter_first()
        while iter:
            name = self.model.get_value(iter, 0)
            if id == name:
                self.model.set_value(iter, 2, b)
                return
            c_iter = self.model.iter_children(iter)
            while c_iter:
                c_name = self.model.get_value(c_iter, 0)
                if id == c_name:
                    self.model.set_value(c_iter, 2, b)
                    return
                c_iter = self.model.iter_next(c_iter)
            iter = self.model.iter_next(iter)

    def save_layout(self, widget, data):
        prefs_set_physical_layout_by_name(self._get_source_layout_id())

    def toggle_cb(self, cell, path, user_data):
        iter = self.model.get_iter(path)
        selected = self.model.get_value(iter, 0)
        current_id = self._get_source_layout_id()
        if selected != current_id:
            self._set_select_layout(current_id, False)
            self.model.set_value(iter, 2, True)
            self._set_source_layout_id(selected)


# Utility function - turn layout name (ex: "fr", "ru" or "us/euro") to
#                    list of xkb_rules.Layout object
#
def layout_make_object_list(name_list):
    all_layouts = prefs_get_layouts()
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
    
#--------------------------------------------------
if __name__ == '__main__':
    def _get_layout_pane():
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)

        view = TargetLayoutList().get_view()
        scrolled_window.add_with_viewport(view)
        scrolled_window.set_size_request(400, 400)
        return scrolled_window

    def _main():
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title(UI_TITLE)
        window.set_size_request(400, 500)
        window.connect("delete_event", lambda w, e: gtk.main_quit())
        scrolled_window = _get_layout_pane()
        window.add(scrolled_window)
        window.show_all()

        gtk.main()

    _main()
