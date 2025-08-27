On linux all the commands must be run as `root` or the user must be added to the `docker` group (then re-log themself in).

### check if the `docker` group exists

    $ getent group docker

### add user to `docker` group

    $ sudo useradd/usermod -aG docker $(whoami)

    # or

    $ sudo adduser $(whoami) docker
