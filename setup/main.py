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
import getopt
import sys
import os
import gettext

import layout
import hotkey
from vars import *
        
def ok_cb(widget, data):
    gtk.main_quit()
    return False

def cancel_cb(widget):
    gtk.main_quit()
    return False
    
def help_cb(widget, data):
    _show_help()
    return False

def print_help(out, v=0):
    print >> out, "-k        # virtual keyboard symbol list config"
    print >> out, "-c <file> # re-create xkbc.dat data file"
    sys.exit(v)

def _show_help():
    try:
        import gnome
    except:
        print "You need python gnome module to use this help."
        return

    p = { gnome.PARAM_APP_DATADIR : '/usr/share' }
    gnome.program_init("ibus-xkbc", '1.0', properties=p)
    gnome.help_display("ibus-xkbc")

def main():

    # -------------------------------------------------------------
    # Re-create ibus-xkbc/data/xkbc.dat
    # this option is for just maintenance purpose
    shortopt = "c:k"
    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopt)
    except:
        print_help(sys.stderr, 1)

    gettext.bindtextdomain("ibus-xkbc", os.getenv('XKBC_LOCALE_DIR'))
    gettext.bind_textdomain_codeset("ibus-xkbc", "UTF-8")

    vkb_mode = False
    for o, a in opts:
        if o == "-c":
            import prefs
            prefs.recreate_db(a)
            sys.exit(0)
        elif o == "-k":
            vkb_mode = True
        else:
            print_help(sys.stderr, 1)
    # -------------------------------------------------------------

    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    title = UI_TITLE if vkb_mode == False else UI_TITLE_VKB
    window.set_title(title)
    window.set_size_request(400, 500)
    window.connect("delete_event", lambda w, e: gtk.main_quit())

    vbox = gtk.VBox(False, 5)
    notebook = gtk.Notebook()

    # Target Layout
    scrolled_window = gtk.ScrolledWindow()
    scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
    target_layout = layout.TargetLayoutList()
    view = target_layout.get_view()
    scrolled_window.add_with_viewport(view)
    scrolled_window.set_size_request(400, 400)
    
    notebook.append_page(scrolled_window, gtk.Label(UI_LAYOUT_TAB))

    # Source Layout
    scrolled_window = gtk.ScrolledWindow()
    scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
    source_layout = layout.SourceLayoutList()
    view = source_layout.get_view()
    scrolled_window.add_with_viewport(view)
    scrolled_window.set_size_request(400, 400)

    # Hot key
    hotkey_box = gtk.VBox(False, 0)
    cycle_hotkey_list = hotkey.CycleHotkeyList(window)
    hotkey_box.pack_start(cycle_hotkey_list.get_window(), True, False, 0)
    hotkey_box.pack_start(gtk.HSeparator(), False, False, 0)
    rcycle_hotkey_list = hotkey.RCycleHotkeyList(window)
    hotkey_box.pack_start(rcycle_hotkey_list.get_window(), True, False, 0)

    if vkb_mode == False:
        notebook.append_page(scrolled_window, gtk.Label(UI_SOURCE_LAYOUT_TAB))
        notebook.append_page(hotkey_box, gtk.Label(UI_HOTKEY_TAB))

    button_box = gtk.HBox(False, 10)
    ok_button = gtk.Button(UI_OK)
    ok_button.connect("clicked", target_layout.save_layouts, None)
    ok_button.connect("clicked", source_layout.save_layout, None)
    ok_button.connect("clicked", cycle_hotkey_list.save_hotkey, None)
    ok_button.connect("clicked", rcycle_hotkey_list.save_hotkey, None)
    ok_button.connect("clicked", ok_cb, None)
    cancel_button = gtk.Button(UI_CANCEL)
    cancel_button.connect("clicked", cancel_cb)
    help_button = gtk.Button(UI_HELP)
    help_button.connect("clicked", help_cb, notebook)
    button_box.pack_start(ok_button, True, True, 10)
    button_box.pack_start(cancel_button, True, True, 10)
    button_box.pack_end(help_button, True, True, 10)

    vbox.pack_start(notebook, True, True, 0)
    vbox.pack_start(button_box, True, False, 0)

    window.add(vbox)
    window.show_all()

    gtk.main()

if __name__ == '__main__':
    main()

    
    
        
