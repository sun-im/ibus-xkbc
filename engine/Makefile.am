# vim:set noet ts=4:
#
# ibus-tmpl - The Input Bus template project
#
# Copyright (c) 2007-2008 Huang Peng <shawn.p.huang@gmail.com>
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
engine_xkbc_PYTHON = \
	engine.py \
 	factory.py \
	compose_tbl.py \
 	main.py \
 	$(NULL)

engine_xkbcdir = $(datadir)/ibus-xkbc/engine
 
libexec_SCRIPTS = ibus-engine-xkbc
engine_DATA = xkbc.xml
enginedir = $(datadir)/ibus/component

xkbc.xml: xkbc.xml.in
	( \
		libexecdir=${libexecdir}; \
		pkgdatadir=${pkgdatadir}; \
		s=`cat $<`; \
		eval "echo \"$${s}\""; \
	) > $@
 
CLEANFILES = \
	xkbc.xml \
	*.py \
 	*.pyc \
	*.pyo \
 	$(NULL)
 
EXTRA_DIST = \
 	ibus-engine-xkbc.in \
 	xkbc.xml.in \
 	$(NULL)
 
# test:
# 	$(ENV) LANG=en_US PYTHONPATH=$(top_srcdir) $(PYTHON) $(srcdir)/main.py
# 
