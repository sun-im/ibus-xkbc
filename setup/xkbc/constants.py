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

# default data dir
DEF_DATA_DIR = "/usr/X11/share/X11/xkb"

# directory name for each component
DN_SYMBOLS = "symbols"
DN_TYPES = "types"
DN_GEOMETRY = "geometry"
DN_KEYMAP = "keymap"
DN_KEYCODES = "keycodes"

COMMENT_START = "//"
COMMENT_START2 = "#"
BLOCK_START = "{"
BLOCK_END = "}"
NAME_START = "("
NAME_END = ")"
SYM_START = "<"
SYM_END = ">"
LIST_START = "["
LIST_END = "]"
LINE_END = ";"
DEFAULT_NAME = "(default)"
STRIP_DIR = "."
NONGROUP_NAME = "_all_"

KWD_SYMBOLS = "xkb_symbols"
KWD_TYPES = "xkb_types"
KWD_KEYCODES = "xkb_keycodes"
KWD_KEYMAP = "xkb_keymap"
KWD_GEOMETRY = "xkb_geometry"

# symbols specific
KWD_MODIFIER_MAP = "modifier_map"
KWD_TYPE = "type"
KWD_KEY = ["key", "Key"]
KWD_INCLUDE = "include"
KWD_NAME = "name"
KWD_KEY_TYPE = "key.type"
KWD_OVERRIDE = "override"
KWD_REPLACE = "replace"
KWD_AUGMENT = "augment"

KWD_VIRTUAL_MODIFIERS = "virtual_modifiers"
KWD_MAP = "map"
KWD_MODIFIERS = "modifiers"
KWD_LEVEL_NAME = "level_name"

KWD_MINIMUM = "minimum"
KWD_MAXIMUM = "maximum"
KWD_ALIAS = "alias"
KWD_ALTERNATE = "alternate"
KWD_INDICATOR = "indicator"
KWD_VIRTUAL = "virtual"

# geometry specific
KWD_DESCRIPTION = "description"
KWD_WIDTH = "width"
KWD_HEIGHT = "height"
KWD_SHAPE = "shape"
KWD_SHAPE_CORNERRADIUS = "shape.cornerRadius"
KWD_OUTLINE = "outline"
KWD_SOLID = "solid"
KWD_SECTION = "section"
KWD_SECTION_LEFT = "section.left"
KWD_SECTION_TOP = "section.top"
KWD_ROW_LEFT = "row.left"
KWD_ROW_TOP = "row.top"
KWD_KEY_SHAPE = "key.shape"
KWD_KEY_GAP = "key.gap"
KWD_TOP = "top"
KWD_LEFT = "left"
KWD_PRIORITY = "priority"
KWD_ROW = "row"
KWD_ROW_VERTICAL = "row.vertical"
KWD_KEYS = "keys"
KWD_INDICATOR_ONCOLOR = "indicator.onColor"
KWD_INDICATOR_OFFCOLOR = "indicator.offColor"
KWD_INDICATOR_TOP = "indicator.top"
KWD_INDICATOR_SHAPE = "indicator.shape"
KWD_INDICATOR = "indicator"
KWD_INDICATOR_PRIORITY = "indicator.priority"
KWD_INDICATOR_LEFT = "indicator.left"
KWD_TEXT_TOP = "text.top"
KWD_TEXT_COLOR = "text.color"
KWD_TEXT = "text"
KWD_TEXT_FONT = "text.font"
KWD_TEXT_FONTSIZE = "text.fontSize"
KWD_TEXT_FONTWIDTH = "text.fontWidth"
KWD_TEXT_WEIGHT = "text.weight"
KWD_TEXT_SLANT = "text.slant"
KWD_LOGO = "logo"
KWD_CORNERRADIUS = "cornerRadius"
KWD_CORNER = "corner"
KWD_APPROX = "approx"
KWD_PRIMARY = "primary"

KWD_BASE_COLOR = "baseColor"
KWD_LABEL_COLOR = "labelColor"
KWD_KEY_COLOR = "key.color"
KWD_COLOR = "color"
KWD_OVERLAY = "overlay"
KWD_ANGLE = "angle"

# componet type
TYPE_SYMBOLS     = 1 << 0
TYPE_TYPES       = 1 << 1
TYPE_GEOMETRY   = 1 << 2
TYPE_KEYCODES    = 1 << 3
TYPE_KEYMAP     = 1 << 4
TYPE_ALL = TYPE_SYMBOLS | TYPE_TYPES | TYPE_GEOMETRY | TYPE_KEYCODES | TYPE_KEYMAP

HINT_HIDDEN = 1 << 0
HINT_DEFAULT = 1 << 1
HINT_PARTIAL = 1 << 2
HINT_ALPHANUMERIC = 1 << 3
HINT_MODIFIER = 1 << 4
HINT_KEYPAD = 1 << 5
HINT_FUNCTION = 1 << 6
HINT_ALTERNATE = 1 << 7

MAIN_DICT = 0
INCLUDE_LIST = 1
OVERRIDE_DICT = 2
OVERRIDE_LIST = 3
AUGMENT_DICT = 4
AUGMENT_LIST = 5
REPLACE_DICT = 6
REPLACE_LIST = 7

# state constant
ST_LEVEL_2 = ST_SHIFT = 1 << 0
ST_CAPS = 1 << 1
ST_CONTROL = 1 << 2
ST_LEVEL_3 = ST_GROUP_2 = ST_ALT_R = 1 << 7 	# altgraph / modeswitch / shift-level3
ST_ALT_L = 0x4000048
ST_NUM_LOCK = 1 << 10
