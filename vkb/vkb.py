#!/usr/bin/env python
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

import gettext
import os
import sys
import getopt
import gtk

x = [os.getenv('XKBC_LIBDIR'), os.getenv('XKBC_SETUPDIR')]
sys.path = x + sys.path

from prefs import *
from vkb_canvas import *
from vkb_window import *
from vkb_config import *

_ = lambda a : gettext.dgettext("ibus-xkbc", a)

#----------------------------------------------------------
def print_help(out, v=0):
    print >> out, "-i", "# for reset option (x, y, scale, transparency etc...)"
    print >> out, "-h", "# for print this message"
    sys.exit(v)

def main():

    gettext.bindtextdomain("ibus-xkbc", os.getenv('XKBC_LOCALE_DIR'))
    gettext.bind_textdomain_codeset("ibus-xkbc", "UTF-8")

    shortopt = "ih"
    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopt)
    except:
        print_help(sys.stderr, 1)

    for o, a in opts:
        if o == "-i":
            # reset VKBConfig
            vkb_config_reset()
        elif o == "-h":
            print_help(sys.stderr, 0)
        else:
            print_help(sys.stderr, 1)
            
    xkbcdb = prefs_get_xkbc_db()

    window = VKBWindow()
    window.set_title(_("Virtual Keyboard"))
    vkb = VKBCanvas(window, xkbcdb)
    window.set_canvas(vkb)
    window.set_default_size(int(vkb.get_width()), int(vkb.get_height()))
    window.connect("destroy", finalize_vkb)
    if vkb_config_get_x() > -99:
        window.move(vkb_config_get_x(), vkb_config_get_y())
    window.show_all()

    try:
        gtk.main()
    except:
        sys.exit(1)

def finalize_vkb(window):
    # store x, y, x_scale, y_scale

    x, y = window.get_position()
    xs, ys = window.get_scale()
    vkb_config_set_x(x)
    vkb_config_set_y(y)
    vkb_config_set_x_scale(xs)
    vkb_config_set_y_scale(ys)
    
    gtk.main_quit()

def get_user_layouts():
    return prefs_get_user_layouts()

if __name__ == "__main__":
    main()
    
