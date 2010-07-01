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

import dbus.service
import ibus
from ibus import keysyms
from ibus import serializable

IBUS_IFACE_VKB = "org.freedesktop.IBus.VKB"
IBUS_PATH_VKB = "/org/freedesktop/IBus/VKB"

class IVKB(dbus.service.Object):

    signal = lambda **args: \
             dbus.service.signal(dbus_interface=IBUS_IFACE_VKB, **args)

    @signal(signature="v")
    def SendText(self, text): pass

    @signal(signature="uu")
    def SendKey(self, keyval, state): pass
    
class VKBProxy(IVKB):
    def __init__(self, conn):
        super(IVKB, self).__init__(conn, IBUS_PATH_VKB)

class Messenger(object):

    def __init__(self):
        self.connected = False
        try:
            self.vkb = VKBProxy(ibus.Bus().get_dbusconn())
            self.connected = True
        except:
            print "Warning: can not connect to ibus daemon. Virtual keyboard runs just in demo mode."

    def send_text(self, text):
        if self.connected:
            t = serializable.serialize_object(ibus.Text(text))
            self.vkb.SendText(t)

    def send_key(self, keyval, state):
        if self.connected:
            self.vkb.SendKey(keyval, state)

def test():
    vkb = VKBProxy(ibus.Bus().get_dbusconn())

    print "Send VKB String"
    vkb.SendText(serializable.serialize_object(ibus.Text("TEST VKB STRING")))
    
    print "Send Retrun Key"
    vkb.SendKey(keysyms.Return, 0)

    import gobject
    loop = gobject.MainLoop()
    loop.run()

if __name__ == "__main__":
    test()

