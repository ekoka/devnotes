#### Ref: https://docs.docker.com/compose/compose-file/05-services/#volumes
#### See also `volumes_from` to mount volumes from another service or container.

- `volumes` can define multiple types of mounts; `volume`, `bind`, `tmpfs`, or `npipe`

    services:
        backend:
            volumes:
                - type: volume
                    source: db-data
                    target: /data
                    volume:
                        nocopy: true
                - type: bind
                    source: /var/run/postgres/postgres.sock
                    target: /var/run/postgres/postgres.sock

    volumes:
        db-data:

#### short syntax


    VOLUME:CONTAINER_PATH:ACCESS_MODE

    VOLUME: a host path on the platform hosting containers or a volume name
    CONTAINER_PATH: path in container where volume is mounted
    ACCESS_MODE: rw, ro, z (SELinux option) bind mount host content is shared among multiple containers, Z (SELinux option) bind mount host content is private and unshared for other containers.

#### long syntax
- additional fields that can't be expressed in the short syntax
- `type`
- `source`
- `target`
- `read_only`
- `bind`
- `volume`
    - `nocopy`
- `tmpfs`
    - `size`
    - `mode`
` consistency`
