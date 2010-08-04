# vim:set noet ts=4:
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
vkb_xkbc_PYTHON = \
	vkb.py \
	vkb_canvas.py \
	vkb_color.py \
	vkb_config.py \
	vkb_constants.py \
	vkb_key.py \
	vkb_keymodel.py \
	vkb_signal.py \
	vkb_window.py \
	$(NULL)

vkb_xkbcdir = $(datadir)/ibus-xkbc/vkb

bin_SCRIPTS = ibus-keyboard

CLEANFILES = \
	*.py \
	*.pyc \
	*.pyo \
	$(NULL)
 
EXTRA_DIST = \
	ibus-keyboard.in \
	$(NULL)
 
# test:
# 	$(ENV) LANG=en_US PYTHONPATH=$(top_srcdir) $(PYTHON) $(srcdir)/main.py
# 
