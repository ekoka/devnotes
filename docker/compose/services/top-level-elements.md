### Ref: https://docs.docker.com/compose/compose-file/05-services/#volumes

#### Some notable configs
- `build`: defines how to create the docker image for the service.

- `blkio_config` set of config options for block IO limits of a service

- `cpu_count`, `cpu_percent`, `cpu_shares`, etc.

- `cap_add` and `cap_drop` manage container capabilities

- `command`: overrides default command declared by the container image (e.g. Dockerfile `CMD`)

    # e.g.
    command: bundle exec thin -p 3000

    # can also be a list
    command: [ "bundle", "exec", "thin", "-p", "3000" ]

If the value is `null`, the default command is used. If the value is empty (`''` or `[]`) the default command is ignored.

- `configs`: see configs.md

- `container_name`: specify a custom container name

- `depends_on`: startup/shutdown dependencies between services
