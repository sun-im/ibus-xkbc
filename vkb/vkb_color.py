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

import cairo

from vkb_constants import *

def _lighter(c):
    return min(c * 1.4, 1.0)

def _darker(c):
    return c * 0.7

def vkb_make_pattern(cr, x, y, w, h, type):

    if type == VKB_GRADIENT:
        pattern = cairo.LinearGradient(x, y, x + w, y + h)
        pattern.add_color_stop_rgb(0, _lighter(cr[0]), _lighter(cr[1]), _lighter(cr[2]))
        pattern.add_color_stop_rgb(1, _darker(cr[0]), _darker(cr[1]), _darker(cr[2]))
    elif type == VKB_SOLID:
        pattern = cairo.SolidPattern(cr[0], cr[1], cr[2])
    else:
        print "Unknown fill pattern."
        pattern = cairo.SolidPattern(cr[0], cr[1], cr[2])
        
    return pattern

    
    
    
