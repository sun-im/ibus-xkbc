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

import ibus
from vkb_constants import *

class VKBConfig(object):
    def __init__(self):
        try:
            self._config = ibus.Bus().get_config()
        except:
            self._config = _ConfigDummy()

    def clear(self):
        self.set_x(-100)
        self.set_x_scale(1.4)
        self.set_y_scale(1.4)
        self.set_label_style(VKB_ACTIVE_TEXT)
        self.set_surface_style(VKB_GRADIENT)
        self.set_window_style(VKB_NORMAL_WINDOW)
        self.set_transparency(1)
        self.set_window_keep_below(False)

    def get_x(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_X, -100)

    def set_x(self, x):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_X, x)

    def get_y(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_Y, -1)

    def set_y(self, y):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_Y, y)

    def get_x_scale(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_X_SCALE, 1.4)

    def set_x_scale(self, x_scale):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_X_SCALE, x_scale)

    def get_y_scale(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_Y_SCALE, 1.4)

    def set_y_scale(self, y_scale):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_Y_SCALE, y_scale)

    def get_layout(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_LAYOUT, "us(euro)")

    def set_layout(self, layout):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_LAYOUT, layout)

    def get_geometry(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_GEOMETRY, "vkb(simple)")

    def set_geometry(self, geometry):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_GEOMETRY, geometry)

    def get_label_style(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_LABEL_STYLE, VKB_ACTIVE_TEXT)

    def set_label_style(self, style):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_LABEL_STYLE, style)

    def get_surface_style(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_SURFACE_STYLE, VKB_GRADIENT)

    def set_surface_style(self, style):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_SURFACE_STYLE, style)

    def get_window_style(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_WINDOW_STYLE, VKB_NORMAL_WINDOW)

    def set_window_style(self, style):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_WINDOW_STYLE, style)
                               
    def get_transparency(self):
        return float(self._config.get_value(KEY_VKB_SECTION, KEY_VKB_TRANSPARENCY, 100)) / 100

    def set_transparency(self, trans):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_TRANSPARENCY, int(trans * 100))

    def get_window_keep_below(self):
        return self._config.get_value(KEY_VKB_SECTION, KEY_VKB_WINDOW_KEEP_BELOW, False)

    def set_window_keep_below(self, value):
        self._config.set_value(KEY_VKB_SECTION, KEY_VKB_WINDOW_KEEP_BELOW, value)

class _ConfigDummy(object):

    def __init__(self):
        self._dict = {}

    # ignore section
    def get_value(self, section, name, defval):
        try:
            return self._dict[key]
        except:
            return defval

    # ignore section
    def set_value(self, section, name, value):
        self._dict[name] = value

    def unset(self, section, name):
        self._dict[name] = None
        
_conf = VKBConfig()

def vkb_config_get_x():
    return _conf.get_x()
def vkb_config_set_x(value):
    _conf.set_x(value)

def vkb_config_get_y():
    return _conf.get_y()
def vkb_config_set_y(value):
    _conf.set_y(value)

def vkb_config_get_x_scale():
    return _conf.get_x_scale()
def vkb_config_set_x_scale(value):
    _conf.set_x_scale(value)

def vkb_config_get_y_scale():
    return _conf.get_y_scale()
def vkb_config_set_y_scale(value):
    _conf.set_y_scale(value)

def vkb_config_get_layout():
    return _conf.get_layout()
def vkb_config_set_layout(value):
    _conf.set_layout(value)

def vkb_config_get_geometry():
    return _conf.get_geometry()
def vkb_config_set_geometry(value):
    _conf.set_geometry(value)

def vkb_config_get_label_style():
    return _conf.get_label_style()
def vkb_config_set_label_style(value):
    _conf.set_label_style(value)

def vkb_config_get_surface_style():
    return _conf.get_surface_style()
def vkb_config_set_surface_style(value):
    _conf.set_surface_style(value)

def vkb_config_get_window_style():
    return _conf.get_window_style()
def vkb_config_set_window_style(value):
    _conf.set_window_style(value)

def vkb_config_get_transparency():
    return _conf.get_transparency()
def vkb_config_set_transparency(value):
    _conf.set_transparency(value)

def vkb_config_get_window_keep_below():
    return _conf.get_window_keep_below()
def vkb_config_set_window_keep_below(value):
    _conf.set_window_keep_below(value)

def vkb_config_reset():
    _conf.clear()
