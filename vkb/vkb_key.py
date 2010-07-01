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
import gtk
import pango
import cairo

sys.path.append(os.getenv('XKBC_LIBDIR'))

from constants import *
from xkb_geometry import *
from xkb_config import *
from vkb_constants import *
from vkb_color import *

class VKBKey(object):

    def set_state(self, state):
        self.parent.set_state(state)

    def __init__(self, key, parent, model):
        """
              key - xkb_geometry : _Key instance
           parent - VKB main canvas (gtk.DrawingArea)
            model - VKBKeyModel for this VKBKey
           parent.get_geometry() returns XKB_Geometry instance
        """
        shape = parent.get_geometry().get_shape_body(key.get_shape())
        self._parent = parent
        self._model = model
        self._coord_list = shape.get_coord_list()
        self._gap = key.get_gap()
        self._cairo_path = None
        self._highlight = False
        self._key = key
        #self._fill_type = VKB_GRADIENT		# VKB_SOLID
        #self._show_text = VKB_ACTIVE_TEXT 	# VKB_ALL_TEXT
        self._inner_x = 0
        self._inner_y = 0
        self._inner_w = 0
        self._inner_h = 0
        self._outer_x = 0
        self._outer_y = 0
        self._outer_w = 0
        self._outer_h = 0
        self._default_font_size = 5
        self._default_font_size2 = 6

    def contains(self, ctx, x, y):
        if self._cairo_path == None:
            return False
        
        ctx.save()
        ctx.new_path()
        ctx.append_path(self._cairo_path[VKB_OUTER_PATH])
        infill = ctx.in_fill(x, y)
        ctx.restore()
        return infill

    def pressed(self):
        if self._highlight:
            if self._model.lock_key():
                self._set_highlight(False)
                self._model.change_state(self._parent)
            else:
                pass
        else:
            self._set_highlight(True)
            self._model.change_state(self._parent)

    def released(self):
        if self._highlight:
            if self._model.lock_key():
                pass
            else:
                self._set_highlight(False)
                self._model.change_state(self._parent)
        else:
            pass

        self._model.clicked(self._parent.get_state())

    def _set_highlight(self, highlight):
        self._highlight = highlight

    def _get_surface_style(self):
        return self._parent.get_surface_style()

    def _get_label_style(self):
        return self._parent.get_label_style()

    def draw(self, ctx, parent):
        if self._cairo_path and len(self._cairo_path) == 2:
            cr = self._parent.get_colors()
            if self._highlight:
                oc = cr[1]; ic = cr[0]; tc = cr[3]
            else:
                oc = cr[0]; ic = cr[1]; tc = cr[2]
            ia_tc = cr[4] # inactive label color for VKB_ALL_TEXT show mode

            # outer path
            ctx.set_source(vkb_make_pattern(oc, self._outer_x, self._outer_y,
                                            self._outer_w, self._outer_h, self._get_surface_style()))
            ctx.append_path(self._cairo_path[VKB_OUTER_PATH])
            ctx.fill()
            # inner path
            ctx.set_source(vkb_make_pattern(ic, self._inner_x, self._inner_y,
                                            self._inner_w, self._inner_h, self._get_surface_style()))
            ctx.append_path(self._cairo_path[VKB_INNER_PATH])
            # set clipping path so that symbol text does not run over the inner path boundary
            ctx.save()
            ctx.clip_preserve()
            ctx.fill()
            # symbol
            self._draw_text(ctx, parent, tc, ia_tc)
            ctx.restore()
        else:
            raise "VKBKey: init_draw() needs to be called before draw() call."

    def init_draw(self, ctx, x, y, parent):
        # 'ctx' is the cairo.Context
        # 'x' and 'y' is the origin for this key's picture
        #
        # returns advanced width
        x += self._gap
        w = w2 = w3 = 0
        path_tmp = []
        extent_tmp = []
        for coord in self._coord_list:
            point_list = coord.get_point_list()
            point_num = len(point_list)
            if point_num == 0:
                return 0
            elif point_num == 1:
                w = point_list[0][0]
                h = point_list[0][1]
                ctx.rectangle(x, y, w, h)
                extent_tmp.append(ctx.path_extents())
                path_tmp.append(ctx.copy_path())
                ctx.new_path()
            elif point_num == 2:
                x2 = point_list[0][0]
                y2 = point_list[0][1]
                w2 = point_list[1][0] - x2
                h2 = point_list[1][1] - y2
                ctx.rectangle(x + x2, y + y2, w2, h2)
                extent_tmp.append(ctx.path_extents())
                path_tmp.append(ctx.copy_path())
                ctx.new_path()
            else:
                max_x = point_list[0][0]
                px = point_list[0][0]
                py = point_list[0][1]
                ctx.move_to(x + px, y + py)
                for p in point_list[1:]:
                    ctx.line_to(x + p[0], y + p[1])
                    max_x = max(max_x, p[0])
                ctx.close_path()
                w3 = max_x - x
                extent_tmp.append(ctx.path_extents())
                path_tmp.append(ctx.copy_path())
                ctx.new_path()

        advw = max(w, w2, w3)
        # assume path_num is always 2 (outer and inner path)
        if len(path_tmp) != 2:
            print "VKBKey.init_draw() : Something wrong...."
            return 0

        self._cairo_path = []
        out_idx = 0; in_idx = 1

        if extent_tmp[0][0] < extent_tmp[1][0]:		# check left x position to judge outer or inner
            self._cairo_path.append(path_tmp[0])	# VKB_OUTER_PATH
            self._cairo_path.append(path_tmp[1])	# VKB_INNER_PATH
        else:
            self._cairo_path.append(path_tmp[1])	# VKB_INNER_PATH
            self._cairo_path.append(path_tmp[0])	# VKB_OUTER_PATH
            out_idx = 1; in_idx = 0

        # store x, y, w, h for key label rendering
        self._inner_x = extent_tmp[in_idx][0]
        self._inner_y = extent_tmp[in_idx][1]
        self._inner_w = extent_tmp[in_idx][2] - self._inner_x
        self._inner_h = extent_tmp[in_idx][3] - self._inner_y
        self._outer_x = extent_tmp[out_idx][0]
        self._outer_y = extent_tmp[out_idx][1]
        self._outer_w = extent_tmp[out_idx][2] - self._outer_x
        self._outer_h = extent_tmp[out_idx][3] - self._outer_y

        # calculate test position
        # inactive position
        offset_1 = self._default_font_size * 0.2
        offset_2 = self._default_font_size * 1.6
        offset_3 = self._default_font_size * 1.2
        self._tp_x = []
        self._tp_y = []
        self._tp_x.append(self._inner_x + offset_1)
        self._tp_y.append(self._inner_y + self._inner_h - offset_2)
        self._tp_x.append(self._inner_x + offset_1)
        self._tp_y.append(self._inner_y)
        self._tp_x.append(self._inner_x + self._inner_w - offset_3)
        self._tp_y.append(self._inner_y + self._inner_h - offset_2)
        self._tp_x.append(self._inner_x + self._inner_w - offset_3)
        self._tp_y.append(self._inner_y)

        # active position
        offset_2 = self._default_font_size * 1.8
        self._tp_ax = []
        self._tp_ay = []
        self._tp_ax.append(self._inner_x + offset_1)
        self._tp_ay.append(self._inner_y + self._inner_h - offset_2)
        self._tp_ax.append(self._inner_x + offset_1)
        self._tp_ay.append(self._inner_y)
        self._tp_ax.append(self._inner_x + self._inner_w - offset_3)
        self._tp_ay.append(self._inner_y + self._inner_h - offset_2)
        self._tp_ax.append(self._inner_x + self._inner_w - offset_3)
        self._tp_ay.append(self._inner_y)

        self.draw(ctx, parent)

        return advw + self._gap
        
    def _draw_text(self, ctx, parent, tc, ia_tc):
        
        state = self._get_state()
        type = self._model.get_type()

        if self._get_label_style() == VKB_ACTIVE_TEXT or type != VKB_CHAR_KEY:
            font_size = self._default_font_size2 if type == VKB_CHAR_KEY else \
                        self._default_font_size * 0.7
            text = self._model.get_display_label(state)
            if text != None:
                
                layout = parent.create_pango_layout(text)
                layout.set_wrap(pango.WRAP_WORD)
                layout.set_width(int(self._inner_w))
                p_extents = layout.get_pixel_extents()
                font_desc = pango.FontDescription("Sans Serif " + str(font_size))
                layout.set_font_description(font_desc)
                line_n = layout.get_line_count() - 1
                pos_id = 1 if type == VKB_CHAR_KEY else 0
                ctx.move_to(self._tp_ax[pos_id] - p_extents[1][0] * 0.6,
                            self._tp_ay[pos_id] - self._default_font_size * line_n)
                ctx.set_source_rgba(tc[0], tc[1], tc[2])
                ctx.show_layout(layout)
        else:
            font_size = self._default_font_size * 0.8
            if self._get_state() & ST_CAPS:
                add_state = ST_CAPS
            else:
                add_state = 0
            text = []
            text.append(self._model.get_display_label(add_state))
            text.append(self._model.get_display_label(add_state | ST_SHIFT | ST_NUM_LOCK))
            text.append(self._model.get_display_label(add_state | ST_LEVEL_3))
            text.append(self._model.get_display_label(add_state | ST_SHIFT | ST_LEVEL_3))
            active_idx = 3 if state & ST_SHIFT and state & ST_LEVEL_3 else \
                         2 if state & ST_LEVEL_3 else \
                         1 if state & ST_SHIFT or state & ST_NUM_LOCK else 0

            rendered_text = []
            for id in range(4):
                if text[id] == None or text[id] in rendered_text:
                    continue
                layout = parent.create_pango_layout(text[id])
                if id == active_idx:
                    font_desc = pango.FontDescription("Sans Serif " + str(font_size * 1.1))
                    layout.set_font_description(font_desc)
                    line_n = layout.get_line_count() - 1
                    ctx.move_to(self._tp_ax[id], self._tp_ay[id] - line_n * self._default_font_size)
                    ctx.set_source_rgba(tc[0], tc[1], tc[2])
                else:
                    font_desc = pango.FontDescription("Sans Serif " + str(font_size))
                    layout.set_font_description(font_desc)
                    line_n = layout.get_line_count() - 1
                    ctx.move_to(self._tp_x[id], self._tp_y[id] - line_n * self._default_font_size)
                    ctx.set_source_rgba(ia_tc[0], ia_tc[1], ia_tc[2])

                ctx.show_layout(layout)
                rendered_text.append(text[id])
            rendered_text = None
            
    def _get_state(self):
        return self._parent.get_state()
