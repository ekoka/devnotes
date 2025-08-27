
#### Start a container from a base image
Start with a base image and run a container

    $ docker run -it alpine sh

#### Modify the container
From the running container, make some changes (e.g. install software, create files, create users, etc)

    # apk add --update redis
    # cd /
    # mkdir foobar
    # touch barbaz

Note that Docker maps some directories like `/data` to volumes and those changes will not carry over in the snapshot. I.e. these will *not* be registered.

    # cd /data
    # echo "Hello" > hello.txt
    # mkdir abc

#### From another terminal commit a snapshot of the (running or stopped) container
Get the container's id from the command

    $ docker ps --all

or

    $ docker container ls --all

Commit the container's contents to image

    $ docker commit [options] <container> [repository[:tag]]
