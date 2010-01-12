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
