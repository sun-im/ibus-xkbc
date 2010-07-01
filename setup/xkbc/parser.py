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

# parser for xkeyboard-config component data

import os
# constants
from constants import *

class Parser(object):

    # This method needs to be overridden so that
    # returns subclass of XKB_Component
    def get_component_class(self):
        return None

    # This method needs to be overridden so that
    # returns component keyword (ex: xkb_symbols, xkb_types...)
    def get_component_keyword(self):
        return None

    # This method needs to be overridden
    def get_component_dirname(self):
        return None

    # external method
    def get_components(self):
        self._dirname = self.get_component_dirname()
        self.files = self._read_dir(self.basedir + os.sep + self._dirname)
        self._parse()
        return self.compdict

    def __init__(self, basedir):
        self.basedir = basedir
        self.compdict = {}

    # read files in 'dir' recursively and return list of them
    def _read_dir(self, dir):
        # return a list contains all of files in dir
        f_list = []
        self._read_dir_r(dir, ".", f_list) # recursive version
        return f_list

    def _read_dir_r(self, root, dir, f_list):
        for root, dirs, files in os.walk(root + os.sep + dir):
            for f in files:
                if f in dirs:
                    self._read_dir_r(root, f, f_list)
                else:
                    if f.startswith("README") or f.startswith("Makefile") or f.endswith(".dir"):
                        continue
                    full_path = root + os.sep + f
                    f_list.append(full_path)

    def _get_compfile_name(self, filename):
        t1, t2, fname = filename.rpartition(os.sep + self._dirname + os.sep)
        if fname.startswith(STRIP_DIR + os.sep):
            fname = fname[len(STRIP_DIR + os.sep):]
        return fname
    
    def _parse(self):
        for f in self.files:
            self.file_name = self._get_compfile_name(f)
            token_buffer = []
            for line in open(f):
                l = line.strip()
                comment_id = l.find(COMMENT_START)
                if comment_id == 0:
                    continue
                if comment_id > 0:
                    l = l[:comment_id]
                comment_id = l.find(COMMENT_START2)
                if comment_id == 0:
                    continue
                if comment_id > 0:
                    l = l[:comment_id]
                # str.split() is not appropriate as given
                # string may have '}};' or ']};'
                token_buffer.extend(self._expand_tokens(l))
            self._parse_tokens(token_buffer)

    white_space = [' ', '\t', ',']
    block_delimiter = ['[', ']', '{', '}', '=', ';']
    splitter = [',']
    string_delimiter = '"'
    escape = "\\"
    def _expand_tokens(self, line):
        buf = []
        idx = 0
        start = 0
        end = 0
        in_string = False
        in_escape = False
        # split line to token with care of [, ], {, }, and "..."
        for c in line:
            idx += 1
            if in_string:
                if c in self.string_delimiter:
                    if in_escape:
                        end = idx
                        in_escape = False
                    else:
                        in_string = False
                        self._append(buf, start, end, line)
                        start = end = idx
                else:
                    if c in self.escape:
                        in_escape = True
                    elif in_escape:
                        in_escape = False
                    end = idx
            elif c in self.string_delimiter:
                    in_string = True
                    start = end = idx
            elif c in self.white_space:
                self._append(buf, start, end, line)
                start = end = idx
            elif c in self.block_delimiter:
                self._append(buf, start, end, line)
                buf.append(c)
                start = end = idx
            else:
                end = idx

        self._append(buf, start, end, line)
        return buf

    def _append(self, buf, start, end, line):
        if start != end:
            token = line[start:end].strip(",")
            if len(token) > 0:
                buf.append(token)

    def _parse_tokens(self, tokens):
        comp_class = self.get_component_class()
        comp_keyword = self.get_component_keyword()
        xkb_component = comp_class()
        i = 0
        length = len(tokens)
        while i < length:
            token = tokens[i]
            i += 1
            if token in self.hint_map.keys():
                xkb_component.add_hint(self.hint_map[token])
            elif token == comp_keyword:
                if tokens[i] == BLOCK_START:
                    name = self.file_name + DEFAULT_NAME
                else:
                    name = self.file_name + NAME_START + tokens[i] + NAME_END; i += 1
                self.compdict[name] = xkb_component
                xkb_component.set_name(name)
                i += 1
                content, tl = self._get_block(tokens[i:])
                i += tl
                xkb_component.set_content(content)

                if i + len(comp_keyword) < length:
                    xkb_component = comp_class()
            elif token == LINE_END:
                pass
            else:
                raise ParserException(comp_keyword + " - Parse error : " + name + " : " + token)

    def _get_block(self, tokens):
        # retuns a list of token between the frist '{' and
        # corresponding '}'
        i = 0
        content = []
        length = len(tokens)

        while i < length:
            token = tokens[i]
            i += 1
            if token == BLOCK_START:
                segment, tl = self._get_block(tokens[i:])
                i += tl
                content.append(segment)
            elif token == BLOCK_END:
                break
            else:
                content.append(token)

        return content, i

    hint_map = {"hidden" : HINT_HIDDEN, "default" : HINT_DEFAULT,
                "partial" : HINT_PARTIAL, "alphanumeric_keys" : HINT_ALPHANUMERIC,
                "modifier_keys" : HINT_MODIFIER, "keypad_keys" : HINT_KEYPAD,
                "function_keys" : HINT_FUNCTION, "alternate_group" : HINT_ALTERNATE}



class ParserException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
