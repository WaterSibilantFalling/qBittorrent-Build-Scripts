#!/usr/bin/env python
''' this pogram automates the compilation of  qbittorrent and qbittorrent-nox
    it should also, optionally, call the build_libtorrent script 

    The idea is that it is now easy to rebuild qbittorrent, both time and brain
    messing with shit wise
'''

import argparse
import sh
from sh import git, cd, sudo, rm

nice = sh.Command('nice')
nice20 = nice.bake('-n 20')

# --- process the commandline

parser = argparse.ArgumentParser(description='build libtorrent')
# parser.add_argument('--aptinstall',help='apt-get the prerequisites', action='store_true')
parser.add_argument('--gitclone', help='re-git the source code', action='store_true')
parser.add_argument('--configure',  help='re-configure the build', action='store_true')
parser.add_argument('--make',  help='re-Make the build', action='store_true')
parser.add_argument('--headless',  help='make the headless version', action='store_true')

args = parser.parse_args()



# --- install the source code
if args.gitclone:
    print "git clone the source code"
    rm('-fr', 'qBittorrent')
    # # # this can take a LONG time - 8 to 15 minutes; gitbub can be slow
    git.clone('https://github.com/qbittorrent/qBittorrent.git')

cd('qBittorrent')
cmd_configure = sh.Command("./configure")



# --- with GUI
if not args.headless:
    # --- configure
    if args.configure:
        print "configure"

        cmd_configure('--libdir=/usr/lib/i386-linux-gnu/', 'LDFLAGS=-L /usr/local/lib/', '--prefix=/usr/local', "--with-boost-libdir=/usr/lib/i386-linux-gnu/", "--enable-debug", "--disable-dependency-tracking", "--disable-option-checking")
        # no python binding option

    # - make

    if args.make:
        print "make"
        nice = sh.Command('nice')
        nice20 = nice.bake('-n 20')

        sudo('cpufreq-set', '-g powersave')         #reduce CPU
        nice20('make', 'clean') # MUST do make clean
        nice20('make')
        # TODO : collect the stderr and stdout output
        print 'make install'
        #sudo(' checkinstall', '--pkgversion',' 3.4.0alpha')
        sudo('make', 'install')



# --- Headless: qbtitorrent-nox
if args.headless:
    nice20('make', 'clean') # MUST do make clean

    if args.configure:
        print "configure headless"
        cmd_configure('--libdir=/usr/lib/i386-linux-gnu/', 'LDFLAGS=-L /usr/local/lib/','--prefix=/usr/local',"--with-boost-libdir=/usr/lib/i386-linux-gnu/", "--enable-debug", "--disable-gui", "--disable-dependency-tracking", "--disable-option-checking" )

    if args.make:
        print "make headless"
        # - make
        sudo('cpufreq-set', '-g powersave')         #reduce CPU
        nice20('make', 'clean') # MUST do make clean
        nice20('make')
        # TODO : collect the stderr and stdout output
        sudo('make', 'install')



# --- cleanup
#
sudo('cpufreq-set', '-g ondemand')
cd('..')
print '=== done ==='


