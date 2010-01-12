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

import sys
import os

from xml.sax import make_parser
from xml.sax.handler import *

DEFAULT_RULE_FILE = os.path.join(os.getenv('XKB_DATA_DIR'), "rules", "xorg.xml")
rule_file = DEFAULT_RULE_FILE

class Layout:
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.variants = []
        self.selected = False
        
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_desc(self, desc):
        self.desc = desc

    def get_desc(self):
        return self.desc
        
    def add_variants(self, variant):
        self.variants.append(variant)

    def get_variants(self):
        return self.variants

    def set_selected(self, selected):
        self.selected = selected

    def get_selected(self):
        return self.selected

class Variant(Layout):
    def __init__(self):
        Layout.__init__(self)
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_desc(self):
        return self.parent.get_desc() + " / " + self.desc

    def get_name(self):
        return self.parent.get_name() + "(" + self.name + ")"

class DocHandler(ContentHandler):

    SKIP_MODE = 0
    READ_MODE = 1
    LAYOUT_MODE = 2
    VARIANT_MODE =3
    
    def __init__(self):
        self.mode = self.SKIP_MODE
        # self.layouts = []
        self.layouts = {}

    def get_layouts(self):
        return self.layouts
    
    def startDocument(self):
        pass
    
    def endDocument(self):
        pass
    
    def characters(self, content):
        self.content = content
        
    def startElement(self, name, attrs):
        if name == "layoutList":
            self.mode = self.READ_MODE
            return

        if name == "variantList":
            self.mode = self.VARIANT_MODE
            return

        if self.mode == self.SKIP_MODE:
            return

        # READ_MODE
        if name == "layout":
            self.mode = self.LAYOUT_MODE
            self.layout = Layout()
        elif name == "variant":
            self.variant = Variant()
            self.variant.set_parent(self.layout)

    def endElement(self, name):
        if self.mode == self.SKIP_MODE:
            return

        if name == "layoutList":
            self.mode = self.SKIP_MODE
            return

        if name == "name":
            if self.mode == self.LAYOUT_MODE:
                self.layout.set_name(self.content)
            elif self.mode == self.VARIANT_MODE:
                self.variant.set_name(self.content)
        elif name == "description":
            if self.mode == self.LAYOUT_MODE:
                self.layout.set_desc(self.content)
                self.content = None
            elif self.mode == self.VARIANT_MODE:
                self.variant.set_desc(self.content)
                self.content = None
        elif name == "layout":
            #self.layouts.append(self.layout)
            self.layouts[self.layout.get_name()] = self.layout
            self.layout = None
            self.mode = self.READ_MODE
        elif name == "variant":
            self.layout.add_variants(self.variant)
            self.variant = None
        elif name == "layoutList":
            self.mode = self.SKIP_MODE
        elif name == "variantList":
            self.mode = self.LAYOUT_MODE

_all_layouts = None

def xkbc_get_layouts():
    global _all_layouts
    if _all_layouts == None:
        parser = make_parser()
        parser.setFeature(feature_namespaces, False)
        parser.setFeature(feature_external_ges, False)
        parser.setFeature(feature_external_pes, False)
        dh = DocHandler()
        parser.setContentHandler(dh)
        parser.parse(open(rule_file))
        _all_layouts = dh.get_layouts()
        
    return _all_layouts
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        rule_file = sys.argv[1]
        
    layouts = get_xkbc_layouts()
    print "layouts = " + str(len(layouts))
