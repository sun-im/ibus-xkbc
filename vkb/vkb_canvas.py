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
import os

from vkb import *
from vkb_key import *
from vkb_keymodel import *
from vkb_config import *

_ = lambda a : gettext.dgettext("ibus-xkbc", a)

class VKBCanvas(gtk.DrawingArea):

    def set_state(self, state):
        if self._state & state:
            self._state ^= state
        else:
            self._state |= state

    def get_state(self):
        return self._state

    def get_width(self):
        return self._scale_factor_x * (self._kbd_width + self._x_gap * 2)

    def get_height(self):
        return self._scale_factor_y * (self._kbd_height + self._y_gap * 2)

    def get_geometry(self):
        return self._geom

    def get_scale(self):
        return (self._scale_factor_x, self._scale_factor_y)

    def get_colors(self):
        return (self._outer_color, self._inner_color, self._text_color,
                self._text_color_r, self._inactive_text_color)

    def __init__(self, parent, xkbcdb):
        gtk.DrawingArea.__init__(self)

        self._parent = parent
        self._x_gap = 3
        self._y_gap = 3
        self._xkbcdb = xkbcdb
        self._context = None
        self._context_menu = None
        self._key_object_list = None
        self._target_key = None
        self._state = 0

        self._scale_factor_x = vkb_config_get_x_scale()
        self._scale_factor_y = vkb_config_get_y_scale()
        self._geometry_name = vkb_config_get_geometry()
        self._layout_name = vkb_config_get_layout()
        self._surface_style = vkb_config_get_surface_style()
        self._transparency = vkb_config_get_transparency()
        self._window_keep_below = vkb_config_get_window_keep_below()
        self._label_style = vkb_config_get_label_style()
        if vkb_config_get_window_style() == VKB_NORMAL_WINDOW:
            self._window_style = VKB_NORMAL_WINDOW
            self._decoration_type = VKB_DECORATION_TITLE
            self._frame_draw = True
        else:
            self._window_style = VKB_KEYS_ONLY_WINDOW
            self._decoration_type = VKB_DECORATION_NONE
            self._frame_draw = False

        self._setup_geom_data()
        self._set_colors()
        self._move_pos = None

        self.add_events(self.EVENT_MASK)
        self.connect("expose-event", self._expose)
        self.connect("configure-event", self._configure)
        self.connect("button-press-event", self._button_press)
        self.connect("motion-notify-event", self._button_motion)
        self.connect("button-release-event", self._button_release)
        self.connect("style-set", self._style_set)

    def _setup_geom_data(self):
        self._geom = self._xkbcdb.get_geometry_dict()[self._geometry_name]
        self._kbd_width = self._geom.get_width()
        self._kbd_height = self._geom.get_height()

    def _color_adjust(self, color):
        rc = []
        for i in (color.red, color.green, color.blue):
            rc.append(float(i) / 0xffff)
        return rc

    def _set_colors(self):
        style = self.get_style()
        self._outer_color = self._color_adjust(style.bg[gtk.STATE_SELECTED])
        self._inner_color = self._color_adjust(style.bg[gtk.STATE_NORMAL])
        self._text_color = self._color_adjust(style.text[gtk.STATE_NORMAL])
        self._text_color_r = self._color_adjust(style.text[gtk.STATE_SELECTED])
        self._inactive_text_color = self._color_adjust(style.text[gtk.STATE_INSENSITIVE])

    def _style_set(self, widget, prev_style):
        self._set_colors()
        return False

    def _repaint(self):
        self._expose(self, None)

    def _reshape_window(self):
        ctx = self.window.cairo_create()
        ctx.set_source_rgb(self._inner_color[0],
                           self._inner_color[1],
                           self._inner_color[2])
        w = self.get_width()
        h = self.get_height()
        ctx.rectangle(0, 0, w, h)
        ctx.scale(self._scale_factor_x, self._scale_factor_y)
        ctx.fill()
        self._parent.resize(int(self.get_width()), int(self.get_height()))

    def _expose(self, widget, event):
        self.parent.set_opacity(self._transparency)
        self.parent.set_keep_below(self._window_keep_below)
        self._context = ctx = widget.window.cairo_create()
        w = self.get_width()
        h = self.get_height()
        ctx.rectangle(0, 0, w, h)
        ctx.scale(self._scale_factor_x, self._scale_factor_y)
        ctx.clip()
        self._draw(ctx)

        return False
    
    def draw_keys(self, ctx):
        ctx.scale(self._scale_factor_x, self._scale_factor_y)
        self._draw(ctx)

    def fill_kbd(self, ctx):
        w = self.get_width()
        h = self.get_height()
        ctx.rectangle(0, 0, w, h)
        ctx.scale(self._scale_factor_x, self._scale_factor_y)
        ctx.fill()

    def _configure(self, widget, event):
        w = self.get_width()
        h = self.get_height()
        self._scale_factor_x *= event.width / w
        self._scale_factor_y *= event.height / h

        return False

    def _set_layout_name(self, item, layout_name):
        self._layout_name = layout_name
        vkb_config_set_layout(layout_name)
        self._reset_layouts()
        self._repaint()

    def _set_geometry_name(self, item, geometry_name):
        self._geometry_name = geometry_name
        vkb_config_set_geometry(geometry_name)
        self._setup_geom_data()
        self._reshape_window()
        self._reset_layouts()
        self._repaint()

    def _reset_layouts(self):
        self._key_object_list = None
        self._target_key = None
        self._state = 0

    def get_label_style(self):
        return self._label_style

    # "Active label only" context menu item callback
    def _set_label_style(self, item):
        self._label_style = VKB_ACTIVE_TEXT if item.get_active() else VKB_ALL_TEXT
        vkb_config_set_label_style(self._label_style)
        self._repaint()

    # "Gradation surface" context menu item callback
    def _set_surface_style(self, item):
        self._surface_style = VKB_GRADIENT if item.get_active() else VKB_SOLID
        vkb_config_set_surface_style(self._surface_style)
        self._repaint()

    def get_surface_style(self):
        return self._surface_style

    # "Keys only window" context menu item callback
    def _set_window_style(self, item):
        if item.get_active():
            self._frame_draw = False
            self._parent.set_decorated(self._frame_draw)
            self._parent.set_keys_only(True)
            self._window_style = VKB_KEYS_ONLY_WINDOW
        else:
            self._frame_draw = True
            self._parent.set_decorated(self._frame_draw)
            self._parent.set_keys_only(False)
            self._window_style = VKB_NORMAL_WINDOW

        vkb_config_set_window_style(self._window_style)
        w, h = self._parent.get_size()
        self._parent.resize(w, h)

    # "Always below other window" context menu callback
    def _set_window_keep_below(self, item):
        if item.get_active():
            self._window_keep_below = True
        else:
            self._window_keep_below = False
        self.parent.set_keep_below(self._window_keep_below)
        vkb_config_set_window_keep_below(self._window_keep_below)

    # "Layout Config" context menu callback
    def _layout_list_setup(self, item):
        setup_cmd = os.path.join(os.getenv('LIBEXECDIR'), "ibus-setup-xkbc")
        os.spawnv(os.P_NOWAIT, setup_cmd, ("ibus-setup-xkbc", "-k"))

    # "Transparency" context menu callback
    def _set_transparency(self, item, val):
        self._transparency = val
        vkb_config_set_transparency(self._transparency)
        self.parent.set_opacity(self._transparency)

    # "Exit" context menu callback
    def _exit(self, item):
        finalize_vkb(self._parent)

    def _setup_menu_item(self, parent, label, cb, data=None, select= False, radio=False, group=None):

        item = None
        if radio:
            item = gtk.RadioMenuItem(group, label)
        else:
            item = gtk.MenuItem(label)
            
        item.set_active(select)
        item.connect("activate", cb, data)
        item.show()
        parent.append(item)
        return item

    def _setup_menu(self, parent, label, submenu):
        item = gtk.MenuItem(label)
        item.set_submenu(submenu)
        item.show()
        parent.add(item)

    def _get_layout_menu(self):
        menu = gtk.Menu()

        i = None
        selected = prefs_get_user_layouts_from_config()
        for lo in selected:
            sym = lo.get_name()
            label = lo.get_desc()

            select = True if sym == self._layout_name else False
            i = self._setup_menu_item(menu, label, self._set_layout_name, sym, select, True, i)

        return menu

    def _get_geometry_menu(self):
        menu = gtk.Menu()

        i = None
        for gem in ("vkb(simple)", "pc(pc101)", "pc(pc102)", "pc(pc104)", "pc(jp106)", "sun(t6)"):
            select = True if gem == self._geometry_name else False
            i = self._setup_menu_item(menu, gem, self._set_geometry_name, gem, select, True, i)

        return menu

    def _get_transparency_menu(self):
        menu = gtk.Menu()

        i = 1
        it = None
        for trans in ("80%", "60%", "40%", "20%", "0%(Opaque)"):
            d = i * 0.2
            s = True if int(d * 100) == int(self._transparency * 100) else False
            it = self._setup_menu_item(menu, trans, self._set_transparency, data=d, select=s, radio=True, group=it)
            i += 1

        return menu
                                  

    def _add_separator(self, menu):
        separator = gtk.SeparatorMenuItem()
        separator.show()
        menu.add(separator)

    def _create_context_menu(self):

        """
        context menu
        ==============
        Layout ->
        Geometry ->
        --------------
        [x] Active Label only
        --------------
        [x] Gradation Surface
        --------------
        [ ] Keys only window
        """
        menu = gtk.Menu()

        self._setup_menu(menu, _("Layout"), self._get_layout_menu())

        self._setup_menu(menu, _("Geometry"), self._get_geometry_menu())
        
        self._add_separator(menu)

        # label style ("Active label only" - On/Off)
        item = gtk.CheckMenuItem(_("Active label only"))
        item.set_active(self._label_style == VKB_ACTIVE_TEXT)
        item.connect("toggled", self._set_label_style)
        item.show()
        menu.add(item)

        # suface style ("Gradation surface" - On/Off)
        item = gtk.CheckMenuItem(_("Gradation surface"))
        item.set_active(self._surface_style == VKB_GRADIENT)
        item.connect("toggled", self._set_surface_style)
        item.show()
        menu.add(item)

        # window shape style ("Keys only" - On/Off)
        item = gtk.CheckMenuItem(_("Keys only window"))
        item.set_active(self._window_style == VKB_KEYS_ONLY_WINDOW)
        item.connect("toggled", self._set_window_style)
        item.show()
        menu.add(item)

        # window keep below other windows
        item = gtk.CheckMenuItem(_("Always below other windows"))
        item.set_active(self._window_keep_below == True)
        item.connect("toggled", self._set_window_keep_below)
        item.show()
        menu.add(item)

        self._add_separator(menu)

        # layout list setup ("Layout list config...")
        item = gtk.MenuItem(_("Layout list config..."))
        item.connect("activate", self._layout_list_setup)
        item.show()
        menu.add(item)

        self._add_separator(menu)

        # Transparency menu is available only if running X11 window manager supports it.
        if self.parent.is_composited():
            self._setup_menu(menu, _("Transparency"), self._get_transparency_menu())
            self._add_separator(menu)

        # exit menu item
        item = gtk.MenuItem(_("Exit"))
        item.connect("activate", self._exit)
        item.show()
        menu.add(item)

        return menu

    def _button_press(self, widget, event):
        
        # popping up context menu event
        if event.button == 3:
            if True: # self._context_menu == None:
                self._context_menu = self._create_context_menu()
            self._context_menu.popup(None, None, None, event.button, event.time)
            return

        # positioning window event
        if event.get_state() & gtk.gdk.MOD4_MASK:
            pos = self._parent.get_position()
            if len(pos) != 2:
                return
            press_pos = event.get_root_coords()
            if len(press_pos) != 2:
                return
            self._move_pos = (press_pos[0] - pos[0], press_pos[1] - pos[1])
            return
        
        ts = self.get_state()
        x = event.x / self._scale_factor_x
        y = event.y / self._scale_factor_y
        self._target_key = self._find_key(x, y)
        if self._target_key:
            self._target_key.pressed()
            s = self.get_state()
            if s != ts:
                self._repaint()
            else:
                self._draw_target(widget, self._target_key)
    

    def _button_motion(self, widget, event):
        if self._move_pos == None or not event.get_state() & gtk.gdk.MOD4_MASK:
            return

        new_pos = event.get_root_coords()
        if len(new_pos) < 2:
            return

        self._parent.move(new_pos[0] - self._move_pos[0], new_pos[1] - self._move_pos[1])

    def _button_release(self, widget, event):
        if self._move_pos != None:
            self._move_pos = None
            return
        
        if self._target_key:
            self._target_key.released()
            self._draw_target(widget, self._target_key)

    def _find_key(self, x, y):
        if self._key_object_list == None:
            return None

        for key in self._key_object_list:
            if key.contains(self._context, x, y):
                return key

        return None

    def _draw_target(self, widget, target_key):
        self._context = widget.window.cairo_create()
        self._context.set_line_cap(cairo.LINE_CAP_ROUND)
        self._context.set_line_width(0.5)
        self._context.scale(self._scale_factor_x, self._scale_factor_y)
        target_key.draw(self._context, self)

    def _draw(self, ctx):
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_line_width(0.5)

        if self._frame_draw:
            self._draw_frame(ctx)

        if self._key_object_list != None:
            for kobj in self._key_object_list:
                kobj.draw(ctx, self)
            return

        self._key_object_list = []
        section_list = self._geom.get_sections()
        for section in section_list:
            name = section.get_name()
            self._draw_section(ctx, section)

    def _draw_frame(self, ctx):
        cr = self.get_colors()
        ctx.set_source_rgb(cr[0][0], cr[0][1], cr[0][2])
        ctx.rectangle(self._x_gap, self._y_gap,
                      self._kbd_width, self._kbd_height)
        ctx.set_line_width(2)
        ctx.stroke()

    def _draw_section(self, ctx, section):
        section_left = section.get_left()
        section_top = section.get_top()

        row_list = section.get_row_list()
        for row in row_list:
            self._draw_row(ctx, row, section_left, section_top)

    def _draw_row(self, ctx, row, section_left, section_top):
        x = row.get_left() + section_left
        y = row.get_top() + section_top

        key_list = row.get_key_list()
        for key in key_list:
            model = vkb_keymodel_get_key_model(self._xkbcdb, self._layout_name, key.get_name())
            vkey = VKBKey(key, self, model)
            x += vkey.init_draw(ctx, x, y, self)
            self._key_object_list.append(vkey)
            
    EVENT_MASK = \
               gtk.gdk.EXPOSURE_MASK | \
               gtk.gdk.STRUCTURE_MASK | \
               gtk.gdk.ENTER_NOTIFY_MASK | \
               gtk.gdk.LEAVE_NOTIFY_MASK | \
               gtk.gdk.BUTTON_PRESS_MASK | \
               gtk.gdk.BUTTON_MOTION_MASK | \
               gtk.gdk.BUTTON_RELEASE_MASK
