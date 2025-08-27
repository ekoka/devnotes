## Installing Docker and Compose on Arch

- ref: https://wiki.archlinux.org/title/Docker

#### Install `docker` and `docker-compose` packages

    $ sudo pacman -S docker
    $ sudo pacman -S docker-compose

    # or for development version

    $ sudo pacman -S docker-git

#### enable/start `docker.service` or `docker.socket`
- `docker.service` starts the service on boot whereas `docker.socket` starts it on first use, which can decrease boot time.

    $ sudo systemctl service enable docker.socket
    $ sudo systemctl service start docker.socket

#### Check docker status 

 - will connect to socket, which will start the service.

    sudo docker info

#### Running `docker` as non-root user group 
- add yourself to the `docker` group 

    sudo usermod -a -G docker mike

