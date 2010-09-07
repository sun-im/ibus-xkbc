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
#
import gettext

_ = lambda a : gettext.dgettext("ibus-xkbc", a)

UI_TITLE = _("XKBC Configuration")
UI_TITLE_VKB = _("Virtual Keyboard layout Configuration")
UI_LAYOUT_TAB = _("Target Layout")
UI_SOURCE_LAYOUT_TAB = _("Physical Layout")
UI_HOTKEY_TAB = _("Hot Keys")

UI_OK = _("_OK")
UI_CANCEL = _("_Cancel")
UI_HELP = _("_Help")

UI_KEYS = _("Hot key")
UI_ADD = _("Add...")
UI_DEL = _("Delete")
UI_ADD2 = _("_Add")
UI_TYPEMSG = _("Please type here.")
UI_ADD_DIALOG_TITLE = _("Hotkey add dialog")

UI_LAYOUT_COLUMN = _("Layout")
UI_SELECT_COLUMN = _("Select")
UI_CYCLE_KEY = _("Switch layout hot keys")
UI_RCYCLE_KEY = _("Switch layout reverse order hot keys")

DEFAULT_LAYOUTS = ["ru", "ara", "gr", "fr", "vn", "th", "us/euro"]
DEFAULT_PHYSICAL_LAYOUT = "us"
DEFAULT_CYCLE_HOTKEY = ["Shift+Control+greater"]
DEFAULT_RCYCLE_HOTKEY = ["Shift+Control+less"]
DEFAULT_COMPOSE_TRIGGERS = ["Multi_key"]

KEY_ROOT = "engine/xkbc"
KEY_USER_LAYOUT = "user_layout"
KEY_PHYSICAL_LAYOUT = "physical_layout"
KEY_CYCLE_HOTKEY = "cycle_hotkey"
KEY_RCYCLE_HOTKEY = "rcycle_hotkey"
KEY_LAST_LAYOUT = "last_layout"

CMD_LAYOUT_SWITCH = "LayoutSwitch"
CMD_SETUP = "Setup"

UI_TOOLTIP_SETUP = _("Configure Layout Switch")

