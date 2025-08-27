### Container 
- running instance that encapsulates required software.
- they're always created from *images*.
- they expose *ports* and *volume* to interact with other containers and/or the outer world
- they can be easily killed, removed, or recreated in a short time.
- they don't keep state.

### Image
- basic element for every *container*.
- when creating an image, every step is cached and can be reused ("Copy On Write" model).
- depending on the image, it can take some time to build.
- on the other hand, a container can be started from the image right away.

### Port
- a tcp/udp port in its original meaning.
- ports can be exposed to the outer world (accessible from the host OS), or connected to other containers (i.e. accessible only from those containers and invisible to the outer world))

### Volume
- similar to a shared folder.
- initialized when a container is created.
- designed to persist data, independent of the container's lifecycle.

### Registry
- a server where docker images are stored (similar to Github).
- an image can be pulled from the registry and deploy it locally.
- an image can also be built locally and pushed to a registry.

### Docker Hub
- a catered registry provided by Docker Inc.
- it's the source of "official" images prepared by the Docker team, or in collaboration with the original software maker (like an OS distro's repository).

