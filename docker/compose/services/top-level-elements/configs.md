#### `configs` top-level service config
- allow services to adapt their behavior without having to rebuild an image
- services can only access configs when explicitly granted the `configs` attribute

###### short syntax
- only specifies the config name, which grants the container access to the config and mounts it as files into the service's container's filesystem (default location `/<config_name>`).

    services:
      redis:
        ...
        configs:
          - my_config
          - my_other_config

    configs:
      my_config:
        file: ./my_config.txt           # value of config is set to contents of file
      my_other_config:
        external: true                  # has already been defined in the platform

##### long syntax
- more granularity

    services:
      redis:
        configs:
          - source: my_config
            target: /redis_config
            uid: "103"
            gid: "103"
            mode: 0440

    configs:
      my_config:
        external: true
      my_other_config:
        external: true
