#!/bin/bash
set -e
set -x

glib-gettextize --force --copy || exit 1
libtoolize --automake --copy --force
aclocal -I m4 --force
autoheader --force
automake --add-missing --copy --force
autoconf --force
export CFLAGS="-g -O0 -Wl,--no-undefined"
export CXXFLAGS="$CFLAGS"
./configure --enable-maintainer-mode $*

