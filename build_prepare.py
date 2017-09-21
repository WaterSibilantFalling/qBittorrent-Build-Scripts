#!/usr/bin/env python

''' thiis program prepares for qbittorrent and libtorrent to be built
    currently is only installs the needed libraries, if they are not already
    installed

    The user running this program must, of couse, have sudo access to apt-get
'''


from sh import sudo
from sh.contrib import git
apt_get_install = sudo.bake('apt-get', 'install')

packages_required_for_qbittorent_and_libtorrent = [
    "libqt5svg5-dev",
    "libboost-system-dev",
    "libboost-dev",
    "libboost-chrono-dev",
    "libboost-random-dev",
    "libssl-dev",
    "libgeoip-dev" "git",
    "pkg-config",
    "automake",
    "libtool",
    "libboost-python-dev",
    "libzip-dev",
    "libzzip-dev",
    "checkinstall",
    "libssl-dev",
    "libgeoip-dev",
    "geoip-database"]

def instal_a_package(pkg_name):
    return_value = apt_get_install(pkg_name)
    if (return_value != 0):
        print "could not apt-get {}. Please investigate".format(pkg_name)
        return -1
    return 0


# --- prerequisites

print "apt-get installing prerequisites"

error_val = 0
for this_package in packages_required_for_qbittorent_and_libtorrent:
    error_val = instal_a_package(this_package);
    if (error_val != 0):
        print "dying"
        break;

if (error_val == 0):
    print "all prerequisites have been installed"





