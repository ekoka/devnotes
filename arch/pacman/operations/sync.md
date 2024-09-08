## -S, --sync
- synchronize packages

- packages and all required deps are installed directly from remote repositories

    dowload and install qt and all its deps
    # pacman -S qt

- specifying the repo (a package may exist in multiple ones)

    # pacman -S testing/qt

- specifying the version

    # pacman -S "bash>=3.2"

    the quotes above are needed for '>', which the shell normally understands as redirection to a file

- specify a group to install from. 

    # pacman -S gnome

    - A numbered list of packages is then displayed to select which to install. 
    - The selection can be of the forms:
        - list of specific packages 
            3 7 8
            1,2,5,7
        - range of packages 
            1-5  # 1 to 5 inclusive
        - exclude packages or range of packages
            ^7 ^3 
            ^1-5

- packages that provide other packages are also considered. i.e. if a requested package is not found, but another provide the same functionality, the latter will be installed. If there are many candidates, a selection prompt is provided.

- upgrading all out-of-date packages

    # pacman -Su

    - version comparison for upgrade
        - alphanum: 1.0a < 1.0b < 1.0beta < 1.0p < 1.0pre < 1.0rc < 1.0.a < 1.0.1
        - numeric: 1 < 1.0 < 1.1 < 1.1.1 < 1.2 < 2.0 < 3.0.0

    - version strings can also have an `epoch` value with the format "epoch:version-rel". The epoch will overrule any version comparison, unless the `epoch` values are equal.

       1:3.6-1 < 2:1.0-1 

## -Sy to download fresh package database from the server (-yy to force refresh, even if up to date) 

    pacman -Sy
