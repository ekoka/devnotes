### Build and run

    $ docker compose up

### run in the background ("detached" mode)

    $ docker compose up -d

### force rebuild

    $ docker compose run up --build

### run a one-off command in a service

    # e.g. run the `env` shell command (list of environment variables) in the `web` service
    $ docker compose run web env

### Run interactive shell after starting container
    
    $ docker-compose exec <service> <shell>
    # e.g.
    $ docker-compose exec db bash
    $ docker-compose exec app sh


### Also see attaching to running container from docker directly (i.e. not through compose)

    $ docker exec -it b0ade48c7df npm run test
    
