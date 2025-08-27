### `depends_on` services top-level element
- startup/shutdown dependencies between services

###### short syntax
- only specify service names of the dependencies

    services:
      web:
        build: .
        depends_on:
          - db
          - redis
      redis:
        image: redis
      db:
        image: postgres


###### long syntax
- enables configuration of additional fields
- `restart`: restart this service after dependency service is updated. Applies to explicit restart controlled by a Compose operation. Excludes automated restart by container runtime after container dies.
- `condition`: sets condition under which dependency is considered satisfied.
- `required`: if `false`, only warns when a service isn't started or available.

    services:
      web:
        build: .
        depends_on:
          db:
            condition: service_healthy
            restart: true
          redis:
            condition: service_started
      redis:
        image: redis
      db:
        image: postgres
