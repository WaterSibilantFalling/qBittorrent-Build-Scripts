
# qbittorrent build scripts

These three small python scripts take over teh job of building qBittorrent and libtorrent on a GNU/Linux, Debian-like system. 

# The Scripts

There are three scripts:

### build\_prepare.py

build\_prepare.py uses apt-get to install all of the prerequisite libraries.

### build\_libtorrent.py

Uses git to download the latest appropriate liborrent code, and then builds & installs the new libtorrent. If building twice, or again due to some problem, wether to ```git clone``` the code and whether to ```./configure``` the Makefile are set by commandline options.

```

me > ./build_libtorrent.py -h
usage: build_libtorrent.py [-h] [--gitclone] [--configure]

build libtorrent

optional arguments:
  -h, --help   show this help message and exit
  --gitclone   re-git the source code
  --configure  re-configure the build

```

### build\_qbittorrent.py 

As for build\_libtorrent.py, uses git to download the most up to date code, builds and then installs qBittorrent. This build uses the latest available libtorrent library. Using commandline parameters the user determines whether to ```git clone``` qBittorrent's source code, to ```./configure``` the make file, to ```make``` and ```make install``` and whether or not to make a headless build ```--headless```.

build\_qbittorrent.py can build either, or both, qBittorrent and qBittorrent-nox


```

me > ./build_qbt.py -h
usage: build_qbt.py [-h] [--gitclone] [--configure] [--make] [--headless]

build libtorrent

optional arguments:
  -h, --help   show this help message and exit
  --gitclone   re-git the source code
  --configure  re-configure the build
  --make       re-Make the build
  --headless   make the headless version

```

