- pacman will attempt to read `pacman.conf` each time it's invoked.

- the file is divided into sections or repositories.

- each section defines a package repository that pacman can use when searching for packages in `--sync` mode, except for the `options` section, which defines global options.

    e.g.

    #
    # pacman.conf
    #
    [options]
    NoUpgrade = etc/passwd etc/group etc/shadow
    NoUpgrade = etc/fstab

    [core]
    Include = /etc/pacman.d/core

    [custom]
    Server = file:///home/pkgs

- each directive must be in CamelCase else it won't be recognized (e.g. noupgrade or NOUPGRADE won't work)


