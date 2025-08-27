- default path : in order of preference `compose.yaml`, `compose.yml`, `docker-compose.yaml`, `docker-compose.yml`
- fragments and extensions can be used to keep the compose file efficient and organized.

### Merging files
- simple attributes and maps are overridden by the highest order compose file
- working with multiple compose files https://docs.docker.com/compose/multiple-compose-files/
- use `include` to factor out parts of the app model, or reuse compose files.


#### Example
The example application is composed of the following parts:

- 2 services, backed by Docker images: webapp and database
- 1 secret (HTTPS certificate), injected into the frontend
- 1 configuration (HTTP), injected into the frontend
- 1 persistent volume, attached to the backend
- 2 networks

    services:
        frontend:
            image: example/webapp
            ports:
            - "443:8043"
            networks:
            - front-tier
            - back-tier
            configs:
            - httpd-config
            secrets:
            - server-certificate

        backend:
            image: example/database
            volumes:
            - db-data:/etc/data
            networks:
            - back-tier

    volumes:
        db-data:
            driver: flocker
            driver_opts:
            size: "10GiB"

    configs:
        httpd-config:
            external: true

    secrets:
        server-certificate:
            external: true

    networks:
        # The presence of these objects is sufficient to define them
        front-tier: {}
        back-tier: {}
