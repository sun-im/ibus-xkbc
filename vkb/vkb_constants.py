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

VKB_OUTER_PATH = 0
VKB_INNER_PATH = 1

VKB_CHAR_KEY = 0
VKB_FUNC_KEY = 1
VKB_MODIFIER_KEY = 2
VKB_CONTROL_KEY = 3
VKB_LOCK_KEY = 4
VKB_KEYPAD_KEY = 5

VKB_SOLID = 0
VKB_GRADIENT = 1

VKB_ALL_TEXT = 0
VKB_ACTIVE_TEXT = 1

VKB_NORMAL_WINDOW = 0
VKB_KEYS_ONLY_WINDOW = 1

VKB_DECORATION_TITLE = 0
VKB_DECORATION_FRAME = 1
VKB_DECORATION_NONE = 2

VKB_DEFAULT_GEOM_NAME = "vkb(simple)"
VKB_DEFAULT_SYM_NAME = "us(euro)"

KEY_VKB_SECTION = "engine/xkbc/vkb"
KEY_VKB_X = "x"
KEY_VKB_Y = "y"
KEY_VKB_X_SCALE = "x_scale"
KEY_VKB_Y_SCALE = "y_scale"
KEY_VKB_LAYOUT = "layout"
KEY_VKB_GEOMETRY= "geometry"
KEY_VKB_LABEL_STYLE = "label_style"
KEY_VKB_SURFACE_STYLE = "surface_style"
KEY_VKB_WINDOW_STYLE = "window_style"
KEY_VKB_TRANSPARENCY = "transparency"
KEY_VKB_WINDOW_KEEP_BELOW = "window_keep_below"
