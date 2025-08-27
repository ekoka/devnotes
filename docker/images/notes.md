ref: https://hackernoon.com/docker-tutorial-getting-started-with-python-redis-and-nginx-81a9d740d091

###  adding an image from the docker registry locally

    # e.g. adding busybox
    $ docker pull busybox

building an image

    $ docker build . -t test-curl

### listing images

    $ docker images

### Best practice for creating images

- include only the necessary context - use a .dockerignore file
- avoid installing unecessary packages
- use cache. place contexts that change frequently (e.g. project's source code) at the end of Dockerfile, it will use the cache effectively.
- be careful with volumes. They're persistent and don't die with containers. The next container may use data left by the previous.
- use environment variable (RUN, EXPOSE, VOLUME). It makes the Dockerfile more flexible.

### Alpine images

- Alpine Linux is a lightweight distro that allows to reduce the overall size of Docker images.
- many Docker images are created on top of it.
- recommended to use images based on Alpine for third-party services, such as Redis, Postgres, etc.
- For app images, use images based on buildpack, it will be easy to debug inside the container and it comes preinstalled with much system-wide required libraries.
- you can get a maximum of benefit from using one basic image for all images, because then, the cache will be used more effectively.

- you can search for images with `docker search`

- base images: images that have no parent image (usually images with an OS, such as ubuntu, busybox, debian)
- child images: images built on base images with additional functionality.
