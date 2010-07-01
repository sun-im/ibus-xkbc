#!/usr/bin/env python
#
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

from constants import *
from parser import *

class GeometryParser(Parser):

    def __init__(self, basedir):
        Parser.__init__(self, basedir)

    def get_component_class(self):
        return XKB_Geometry

    def get_component_keyword(self):
        return KWD_GEOMETRY

    def get_component_dirname(self):
        return DN_GEOMETRY

from xkb_component import XKB_Component

class XKB_Geometry(XKB_Component):

    # ------------ Public interfaces ----------------
    def get_sections(self):
        return self._section_list

    def get_width(self):
        if self._width:
            return self._width
        return 100

    def get_height(self):
        if self._height:
            return self._height
        return 100

    def get_section_left(self):
        if self._section_left:
            return self._section_left
        return 0

    def get_section_top(self):
        if self._section_top:
            return self._section_top
        return 0

    def get_key_gap(self):
        if self._key_gap:
            return self._key_gap
        return 0

    def get_row_left(self):
        if self._row_left:
            return self._row_left
        return 0

    def get_row_top(self):
        if self._row_top:
            return self._row_top
        return 0

    def get_key_shape(self):
        if self._key_shape:
            return self._key_shape
        return "NORM"

    def get_key_color(self):
        if self._key_color:
            return self._key_color
        if self._color:
            return self._color
        return "gray10"

    def get_key_gap(self):
        if self._key_gap:
            return self._key_gap
        return 1

    def get_shape_body(self, name):
        if self._shape_dict.has_key(name):
            return self._shape_dict[name]
        print "Unknown shape :", name
        return self._shape_dict["NORM"]

    # ------------------------------------------------
    
    def __init__(self):
        XKB_Component.__init__(self)
        self._description = None
        self._shape_dict = {}
        self._outline_list = []
        self._solid_list = []
        self._indicator_list = []
        self._indicator_onColor = None
        self._indicator_offColor = None
        self._indicator_top = None
        self._indicator_shape = None
        self._indicator_left = None
        self._indicator_priority = None
        self._width = None
        self._height = None
        self._shape_cornerRadius = None
        self._section_list = []
        self._section_left = None
        self._section_top = None
        self._row_left = None
        self._row_top = None
        self._key_shape = None
        self._key_gap = None
        self._key_color = None
        self._base_color = None
        self._label_color = None
        self._text_top = None
        self._text_color = None
        self._text_font = None
        self._text_fontSize = None
        self._text_fontWidth = None
        self._text_weight = None
        self._text_slant = None
        self._text_list = []
        self._alias_dict = {}
        self._include_list = []
        self._color = None
        self._logo_list = []

    def set_content(self, content):
        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1

            if token == KWD_DESCRIPTION:
                self._description = content[i + 1]; i += 3
            elif token == KWD_WIDTH:
                self._width = float(content[i + 1]); i += 3
            elif token == KWD_HEIGHT:
                self._height = float(content[i + 1]); i += 3
            elif token == KWD_SHAPE_CORNERRADIUS:
                self._shape_cornerRadius = float(content[i + 1]); i += 3
            elif token == KWD_SHAPE:
                shape_name = content[i]
                try:
                    self._shape_dict[shape_name] = _Shape(content[i + 1]); i+= 3
                except:
                    print self.get_name(), shape_name, content[i + 1]
            elif token == KWD_OUTLINE:
                self._outline_list.append(_Outline(content[i], content[i + 1])); i += 3
            elif token == KWD_SECTION_LEFT:
                self._section_left = float(content[i + 1]); i += 3
            elif token == KWD_SECTION_TOP:
                self._section_top = float(content[i + 1]); i += 3
            elif token == KWD_ROW_LEFT:
                self._row_left = float(content[i + 1]); i += 3
            elif token == KWD_ROW_TOP:
                self._row_top = float(content[i + 1]); i += 3
            elif token == KWD_ROW_VERTICAL:
                self._row_vertical = bool(content[i + 1]); i += 3
            elif token == KWD_KEY_SHAPE:
                self._key_shape = content[i + 1]; i += 3
            elif token == KWD_KEY_GAP:
                self._key_gap = float(content[i + 1]); i += 3
            elif token == KWD_SECTION:
                self._section_list.append(_Section(content[i], content[i + 1], self)); i += 3
            elif token == KWD_SOLID:
                self._solid_list.append(_Solid(content[i], content[i + 1])); i += 3
            elif token == KWD_INDICATOR_ONCOLOR:
                self._indicator_onColor = content[i + 1]; i += 3
            elif token == KWD_INDICATOR_OFFCOLOR:
                self._indicator_offColor = content[i + 1]; i += 3
            elif token == KWD_INDICATOR_TOP:
                self._indicator_top = float(content[i + 1]); i += 3
            elif token == KWD_INDICATOR_SHAPE:
                self._indicator_shape = content[i + 1]; i += 3
            elif token == KWD_INDICATOR_LEFT:
                self._indicator_left = float(content[i + 1]); i += 3
            elif token == KWD_INDICATOR:
                self._indicator_list.append(_Indicator(content[i], content[i + 1])); i += 3
            elif token == KWD_TEXT_TOP:
                self._text_top = float(content[i + 1]); i += 3
            elif token == KWD_TEXT_COLOR:
                self._text_color = content[i + 1]; i += 3
            elif token == KWD_TEXT_FONT:
                self._text_font = content[i + 1]; i += 3
            elif token == KWD_TEXT_FONTSIZE:
                self._text_fontSize = float(content[i + 1]); i += 3
            elif token == KWD_TEXT_FONTWIDTH:
                self._text_fontWidth = content[i + 1]; i += 3
            elif token == KWD_TEXT_WEIGHT:
                self._text_weight = content[i + 1]; i += 3
            elif token == KWD_TEXT_SLANT:
                self._text_slant = content[i + 1]; i += 3
            elif token == KWD_TEXT:
                self._text_list.append(_Text(content[i], content[i + 1])); i += 3
            elif token == KWD_ALIAS:
                alias_name = content[i]
                self._alias_dict[alias_name] = content[i + 2]; i += 4
            elif token == KWD_INCLUDE:
                self._include_list.append(content[i]); i += 1
            elif token == KWD_BASE_COLOR:
                self._base_color = content[i + 1]; i += 3
            elif token == KWD_LABEL_COLOR:
                self._label_color = content[i + 1]; i += 3
            elif token == KWD_KEY_COLOR:
                self._key_color = content[i + 1]; i += 3
            elif token == KWD_INDICATOR_PRIORITY:
                self._indicator_priority =  float(content[i + 1]); i += 3
            elif token == KWD_COLOR:
                self._color = content[i + 1]; i += 3
            elif token == KWD_LOGO:
                self._logo_list.append(_Logo(content[i], content[i + 1])); i += 3
            else:
                # raise ParserException("Geometry contents: Parse error: " + self._name + " : " + token)
                print "YET HANDLED", token
            
class _Shape:
    # ------------ Public Interfaces -------------
    def get_coord_list(self):
        return self._coord_list

    # ---------------------------------------------
    def __init__(self, content):
        self._primary = None
        self._approx = None
        self._cornerRadius = None
        self._corner = None
        self._coord_list = []

        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1
            if token == KWD_CORNERRADIUS:
                self._cornerRadius = float(content[i + 1]); i += 2
            elif token == KWD_CORNER:
                self._corner = float(content[i + 1]); i += 2
            elif token == KWD_PRIMARY:
                self._primary = _Coordinate(content[i + 1]); i += 2
            elif token == KWD_APPROX:
                self._primary = _Coordinate(content[i + 1]); i += 2
            elif token == LIST_START:
                # this may be format error entry, but handle it anyway
                # shape "XXXX" {[x, y]} not {{[x, y'}}
                j = i - 1
                while content[i] != LIST_END:
                    i += 1
                i += 1
                token = list(content[j:i])
                self._coord_list.append(_Coordinate(token))
            else:
                self._coord_list.append(_Coordinate(token))
        
class _Coordinate:
    # ------------ Public Interfaces -------------
    def get_point_list(self):
        return self._point_list

    # ---------------------------------------------    
    def __init__(self, content):
        self._point_list = []

        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1
            if token == LIST_START:
                x = float(content[i]); i += 1
                y = float(content[i]); i += 2 # skip LIST_END
                self._point_list.append((x, y))

class _Section:
    # ------------ Public Interfaces -------------
    def get_name(self):
        return self._name

    def get_left(self):
        if self._left:
            return self._left
        return self._parent.get_section_left()

    def get_top(self):
        if self._top:
            return self._top
        return self._parent.get_section_top()

    def get_key_gap(self):
        if self._key_gap:
            return self._key_gap
        return self._parent.get_key_gap()

    def get_row_list(self):
        return self._row_list

    def get_row_left(self):
        if self._row_left:
            return self._row_left
        return self._parent.get_row_left()

    def get_row_top(self):
        if self._row_top:
            return self._row_top
        return self._parent.get_row_top()

    def get_key_shape(self):
        if self._key_shape:
            return self._key_shape
        return self._parent.get_key_shape()

    def get_key_color(self):
        if self._key_color:
            return self._key_color
        return self._parent.get_key_color()

    def get_key_gap(self):
        if self._key_gap:
            return self._key_gap
        return self._parent.get_key_gap()

    # ---------------------------------------------
    def __init__(self, name, content, parent):
        self._name = name
        self._parent = parent
        self._row_list = []
        self._row_vertical = None
        self._row_left = None
        self._row_top = None
        self._top = None
        self._left = None
        self._width = None
        self._height = None
        self._priority = None
        self._key_color = None
        self._key_gap = None
        self._key_shape = None
        self._indicator_top = None
        self._indicator_onColor = None
        self._indicator_offColor = None
        self._indicator_shape = None
        self._indicator_list = []
        self._text_list = []
        self._text_color = None
        self._solid_list = []
        self._overlay_list = []
        self._angle = None

        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1
            if token == KWD_TOP:
                self._top = float(content[i + 1]); i += 3
            elif token == KWD_ROW:
                self._row_list.append(_Row(content[i], self)); i += 2
            elif token == KWD_LEFT:
                self._left = float(content[i + 1]); i += 3
            elif token == KWD_KEY_COLOR:
                self._key_color = content[i + 1]; i += 3
            elif token == KWD_INDICATOR_TOP:
                self._indicator_top = float(content[i + 1]); i += 3
            elif token == KWD_INDICATOR_ONCOLOR:
                self._indicator_onColor = content[i + 1]; i += 3
            elif token == KWD_INDICATOR_OFFCOLOR:
                self._indicator_offColor = content[i + 1]; i += 3
            elif token == KWD_INDICATOR_SHAPE:
                self._indicator_shape = content[i + 1]; i += 3
            elif token == KWD_INDICATOR:
                self._indicator_list.append(_Indicator(content[i], content[i + 1])); i += 3
            elif token == KWD_TEXT:
                self._text_list.append(_Text(content[i], content[i + 1])); i += 3
            elif token == KWD_TEXT_TOP:
                self._text_top = float(content[i + 1]); i += 3
            elif token == KWD_KEY_GAP:
                self._key_gap = float(content[i + 1]); i += 3
            elif token == KWD_KEY_SHAPE:
                self._key_shape = content[i + 1]; i += 3
            elif token == KWD_WIDTH:
                self._width = float(content[i + 1]); i += 3
            elif token == KWD_HEIGHT:
                self._height = float(content[i + 1]); i += 3
            elif token == KWD_PRIORITY:
                self._priority = int(content[i + 1]); i += 3
            elif token == KWD_SOLID:
                self._solid_list.append(_Solid(content[i], content[i + 1])); i += 3
            elif token == KWD_OVERLAY:
                self._overlay_list.append(_Overlay(content[i], content[i + 1])); i += 3
            elif token == KWD_ROW_VERTICAL:
                self._row_vertical = bool(content[i + 1]); i += 3
            elif token == KWD_ANGLE:
                self._angle = float(content[i + 1]); i += 3
            elif token == KWD_ROW_LEFT:
                self._row_left = float(content[i + 1]); i += 3
            elif token == KWD_ROW_TOP:
                self._row_top = float(content[i + 1]); i += 3
            elif token == KWD_TEXT_COLOR:
                self._text_color = content[i + 1]; i += 3
            else:
                print "Unkown: ", token
                
class _Row:
    # ------------ Public Interfaces -------------
    def get_left(self):
        if self._left:
            return self._left
        return self._parent.get_row_left()

    def get_top(self):
        if self._top:
            return self._top
        return self._parent.get_row_top()

    def get_key_list(self):
        if self._keys:
            return self._keys.get_key_list()
        return []

    def get_key_shape(self):
        if self._key_shape:
            return self._key_shape
        return self._parent.get_key_shape()

    def get_key_color(self):
        return self._parent.get_key_color()

    def get_key_gap(self):
        return self._parent.get_key_gap()

    # ----------------------------------------------
    def __init__(self, content, parent):
        self._parent = parent
        self._top = None
        self._left = None
        self._key_shape = None
        self._keys = None

        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1
            if token == KWD_TOP:
                self._top = float(content[i + 1]); i += 3
            elif token == KWD_LEFT:
                self._left = float(content[i + 1]); i += 3
            elif token == KWD_KEY_SHAPE:
                self._key_shape = content[i + 1]; i += 3
            elif token == KWD_KEYS:
                self._keys = _Keys(content[i], self); i += 2
            else:
                "Unkown Row token :", token

class _Keys:
    # ------------ Public Interfaces -------------
    def get_key_list(self):
        return self._key_list

    # ----------------------------------------------
    def __init__(self, content, parent):
        self._parent = parent
        self._key_list = []

        length = len(content)
        i = 0
        while i < length:
            token = content[i]; i += 1
            self._key_list.append(_Key(token, self._parent))
                
class _Key:
    # ------------ Public Interfaces -------------
    def get_name(self):
        if self._name:
            return self._name
        return "<XXXX>" # should never comes here

    def get_shape(self):
        if self._shape:
            return self._shape
        return self._parent.get_key_shape()

    def get_color(self):
        if self._color:
            return self._color
        return self._parent.get_key_color()

    def get_gap(self):
        if self._gap:
            return self._gap
        return self._parent.get_key_gap()

    # ----------------------------------------------    
    def __init__(self, content, parent):
        self._parent = parent
        self._name = None
        self._shape = None
        self._color = None
        self._gap = None

        if type(content) == type(""):
            self._name = content
        else:
            length = len(content)
            i = 0
            while i < length:
                token = content[i]; i += 1
                if token.startswith(SYM_START):
                    self._name = token
                elif token == KWD_COLOR:
                    self._color = content[i + 1]; i += 2
                elif token == KWD_SHAPE:
                    self._shape = content[i + 1]; i += 2
                else:
                    try:
                        gap = float(token)
                        self._gap = gap
                    except:
                        # assume just string in keys array is shape name
                        self._shape = token

class _Outline:
    def __init__(self, name, content):
        self._name = name
        self._content = content

class _Solid:
    def __init__(self, name, content):
        self._name = name
        self._content = content

class _Logo:
    def __init__(self, name, content):
        self._name = name
        self._content = content

class _Indicator:
    def __init__(self, name, content):
        self._name = name
        self._content = content

class _Text:
    def __init__(self, name, content):
        self._name = name
        self._content = content

class _Overlay:
    def __init__(self, name, content):
        self._name = name
        self._content = content

if __name__ == "__main__":
    dir = "/usr/share/X11/xkb"
    geometry_dict = GeometryParser(dir).get_components()


    
