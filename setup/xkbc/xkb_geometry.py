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

__author__="naoyuki"
__date__ ="$Aug 13, 2009 5:23:29 PM$"

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

    def __init__(self):
        XKB_Component.__init__(self)

    def set_content(self, content):
        length = len(content)
        i = 0

