#### Running a container

    $ docker run ubuntu /bin/echo 'Hello world'

- "ubuntu" is the image:  Docker looks first for the image on your Docker host. If not found locally, it's pulled from the public image registry — Docker Hub.
- "/bin/echo ‘Hello world’" is the command run within the new container.

#### Interacting with a shell inside a container

    $ docker run -i -t --rm ubuntu /bin/bash

    `-t` assigns a terminal inside the container.
    `-i` gets a hold of the standard input of the container.
    `--rm` removes the container when the process exits. By default, containers are not deleted.

#### Keeping a container running beyond end of session (i.e. daemonize it)

    $ docker run --name daemon -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"

    `--name daemon` assigns daemon name to a new container. If not specified, Docker assigns one automatically.
    `-d` detaches the terminal and daemonizes the container (i.e. runs it in the background)

#### Other flags

- show all exposed ports with `-P` 

#### checking logs

- see what one specific container is doing  

    $ docker logs -f <container_name or ID>

- the log fetched above is the log of a container
- the -f flag follows the log output (like tail -f) 
- if using the container's ID you can use the first few characters that distinguish it from other containers.

    $ docker logs dc3

#### Starting/Stopping a container

    $ docker start <container_name or ID>
    $ docker stop <container_name or ID>


