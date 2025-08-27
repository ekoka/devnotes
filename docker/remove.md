#### Remove containers

    $ docker rm <container_name or ID>

    # remove all containers
    $ docker rm -f $(docker ps -aq)

    -f remove a container even if it's running (stop and remove)

    ps flags
    -a all containers (running or not)
    -q print only container IDs

- removing all containers with `prune`

    $ docker container prune

#### Remove images

    $ docker rmi
