# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="naoyuki"
__date__ ="$Jul 30, 2009 11:24:47 AM$"

from ConfigParser import ConfigParser

CONFIG_FILE = "xkbc.conf"
config = ConfigParser()
config.read(CONFIG_FILE)

DATA_SECTION = "DATA"
DATA_DIR = "data_dir"


default_data_dir = "/usr/X11/share/X11/xkb"

data_dir = config.get(DATA_SECTION, DATA_DIR)

def get_data_dir():
    return data_dir

def test():
    print "xkb data comes from " + data_dir;

if __name__ == "__main__":
    test()
