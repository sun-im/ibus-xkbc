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

setup_xkbc_PYTHON = \
	__init__.py \
	constants.py \
	parser.py \
	props.py \
	unicodeutil.py \
	xkb_component.py \
	xkb_config.py \
	xkb_geometry.py \
	xkb_keycodes.py \
	xkb_keymap.py \
	xkb_symbols.py \
	xkb_types.py \
	xkb_rules.py \
	$(NULL)

setup_xkbcdir = $(datadir)/ibus-xkbc/setup/xkbc

layout_data_DATA = \
	xkbc.dat \
	$(NULL)

layout_datadir = $(datadir)/ibus-xkbc/data
 
CLEANFILES = \
	*.pyc \
	*.dat \
	$(NULL)
 
# test:
# 	$(ENV) LANG=en_US PYTHONPATH=$(top_srcdir) $(PYTHON) $(srcdir)/main.py
# 
