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

import gtk
import cairo

from vkb_config import *

class VKBWindow(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self)
        self.canvas = None
        self.connect("size-allocate", self._on_size_allocate)
        self._keys_only = vkb_config_get_window_style() == VKB_KEYS_ONLY_WINDOW
        self.set_decorated(not self._keys_only)

    def _on_size_allocate(self, window, allocation):
        if self.canvas == None:
            return
        
        w, h = allocation.width, allocation.height
        bitmap = gtk.gdk.Pixmap(None, w, h, 1)
        ctx = bitmap.cairo_create()
        ctx.set_source_rgb(0.0, 0.0, 0.0)
        ctx.set_operator(cairo.OPERATOR_CLEAR)
        ctx.paint()

        ctx.set_operator(cairo.OPERATOR_SOURCE)

        if self._keys_only:
            self.canvas.draw_keys(ctx)
            # key only window does not take focus
            self.set_property("accept-focus", False)
        else:
            self.canvas.fill_kbd(ctx)
            self.set_property("accept-focus", True)

        window.shape_combine_mask(bitmap, 0, 0)
  
    def set_canvas(self, canvas):
        self.canvas = canvas
        self.add(canvas)

    def set_keys_only(self, trans):
        self._keys_only = trans
        w, h = self.get_size()
        self.resize(w, h)

    def get_scale(self):
        if self.canvas == None:
            return (0, 0)

        return self.canvas.get_scale()
    
