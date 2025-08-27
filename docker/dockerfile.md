ref: https://hackernoon.com/docker-tutorial-getting-started-with-python-redis-and-nginx-81a9d740d091

### Dockerfile

- use to build a Docker image
- a plain text file with instructions and arguments
- instructions

    - FROM : base image
    - RUN : command to execute in the container
    - ENV : set environemnt variables
    - WORKDIR : set working dir
    - VOLUME : create a mount point
    - CMD : set executable for container

example of creating an image:

### Create an image that gets the content of www.example.com and stores it in a text file.

- place the following Dockerfile in a directory

    # Dockerfile

    FROM ubuntu:latest
    RUN apt-get update \
        && apt-get install --no-install-recommends --no-install-suggests -y curl \
        && rm -rf /var/lib/apt/lists/*
    ENV SITE_URL http://www.example.com
    WORKDIR /data
    VOLUME /data
    CMD sh -c "curl -Lk $SITE_URL > /data/results

- cd to the same directory as the Dockerfile and build an image from it

    $ docker build . -t test-curl


    -t sets the name tag on an image

- running a container from the image

    $ docker run --rm -v $(pwd):/data/:rw test-curl

- copy some files from the local directory into a volume in the container

    ADD local_dir /some/dir/in/container

see also: https://docs.docker.com/engine/reference/builder/
