### Ref: https://docs.docker.com/compose/compose-file/05-services/#volumes

#### Some notable configs
- `build`: specifies the build configuration for creating a container image from source, as defined in the [Compose Build Specification](https://docs.docker.com/compose/compose-file/build/).

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

- `depends_on`: see depends\_on.md

- `deploy` configs for deployment and lifecycle of services. See https://docs.docker.com/compose/compose-file/deploy/

- `develop` : specifies development configuration for maintaining a container in sync with source. See https://docs.docker.com/compose/compose-file/develop/

- `dns`, `dns_opt`, `dns_search`: dns control

- `domainname` : custom domain name to use for service container (must be valid RFC 1123 hostname)

- `entrypoint` : default entrypoint for service container. Overrides `ENTRYPOINT` from Dockerfile. If non-null, any default command from the image is ignored (e.g. `CMD` in Dockerfile). If `null` entrypoint from image is used. If empty (`[]` or `''`) default entrypoint in image is ignored.

    # e.g. string
    entrypoint: /code/entrypoint.sh

    # e.g. list
    entrypoint:
      - php
      - -d
      - zend_extension=/usr/local/lib/php/extensions/....
      - memory_limit=-1
      - vendor/bin/phpunit

- `environment`: env variables set in the container. Boolean values should be enclosed in quotes to ensure they're not converted to True or False by the YAML parser.

    # map syntax
    environment:
      RACK_ENV: development
      SHOW: "true"
      USER_INPUT:

    # array syntax
    environment:
      - RACK_ENV=development
      - SHOW=true
      - USER_INPUT

- `env_file` and `environment`: see env\_file.md

- `expose`: defines incoming port or range that Compose exposes from the container. Syntax is `<portnum>[/<protocol>]`. If the Dockerfile for the image already exposes ports, it's visible to other containers on the network, even if `expose` is not set in the Compose file.

    expose:
      - "3000"
      - "8000"
      - "8080-8085/tcp"

- `extends`: share common config among different files or projects.

    services:
      webapp:
        extends:
          file: common.yml
          service: webapp

- `external_links`:  link service containers to services managed outside the Compose app, using the platform lookup mechanism.

    external_links:
      - redis
      - database:mysql
      - database:postgresql

- `extra_hosts`: adds hostname mappings to the container network interface configuration (/etc/hosts).

- `group_add`: specifies additional groups

- `healthcheck`: declares a check that runs to determine whether the service containers are healthy.

- `hostname`: custom host name (valid RFC 1123).

- `image`: specifies image to start the container from. Must follow the Open Container Specification format `[<registery>/][<project>/]<image>[:<tag>|@<digetst>]`

- `ipc`: IPC isolation mode set by the service container.

    ipc: "sharable" # container has its own private IPC namespace, possibly shared with other containers.
    ipc: "service:[namespace]" # makes container join another container's (sharable) IPC namespace.

- `labels`: add metadata to containers. Reverse-DNS notation is recommended to prevent name conflicts.

    labels:
      com.example.description: "Accounting webapp"
      com.example.departnment: "Finance"
      com.example.label-with-empty-value: ""

    labels:
      - "com.example.description=Accounting webapp"
      - "com.example.departnment=Finance"
      - "com.example.label-with-empty-value"

- `links`: defines a network link to containers in another service. Containers for the linked ervice are reachable at a hostname identical to the alias, or the service name. Links aren't required for services to communicate. With no network specified any service is able to reach any other service with their name on the default network. If services declare networks they are attached to, `links` does not override the network config and services not attached to the shared network are not able to communicate.

    web:
      links:
        - db
        - db:database
        - redis

- `logging`: logging configuration for the service.

    logging:
      driver: syslog
      options:
        syslog-address: "tcp://192.168.0.42:123"
