#!/usr/bin/env python

import argparse

from sh import tar, wget, cd
from sh import rm
import sh
from sh import sudo
from sh.contrib import git


parser = argparse.ArgumentParser(
        description='build libtorrent')
parser.add_argument('--gitclone', help='re-git the source code', action='store_true')
parser.add_argument('--configure',  help='re-configure the build', action='store_true')

args = parser.parse_args()



# --- install the source code

if args.gitclone:
    print "git clone the source code"

    # use 1.1.4, not latest and not 1.2, until told otherwise
    rm('-fr', 'libtorrent')
    git.clone('https://github.com/arvidn/libtorrent.git')
    cd('libtorrent')
    git.checkout('RC_1_1')         # gets 1.1.4   <<----- DO THIS 
else:
    # ensure cd to libtorrent
    cd('libtorrent')


# --- configure
if args.configure: 
    print "configure" 

    cmd = sh.Command('./autotool.sh')
    cmd()

    configure = sh.Command("./configure")
    configure( '--libdir=/usr/lib/i386-linux-gnu/', 'LDFLAGS=-L/usr/local/lib/', "--with-boost-libdir=/usr/lib/i386-linux-gnu/", "--enable-encryption", "--prefix=/usr/local/", "--disable-debug", "--enable-python-binding", "--with-boost-python", "LIBS=-ldl")
    # LIBS= hold nonstandard individual LIBRARIES
    #   -dl is is libdl which is to handle non-2.2.5 glibc, for python bindings
    #   see https://github.com/arvidn/libtorrent/issues/1582
    # LDFLAGS=-L<dir> holds non-standard libs DIRS

# --- aake 
print "make"
# make
sudo('cpufreq-set', '-g powersave')         #reduce CPU
nice20=sh.Command('nice', '-n 20') 
nice20('make','clean') 
sudo("make", "uninstall")
nice20('make')

print "make install"
sudo("make", "install")
sudo('cpufreq-set', '-g ondemand')         #restore  CPU


# --- done
cd('..')
print '=== done ==='






