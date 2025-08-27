##### Ref:
- Manual: https://docs.docker.com/compose/environment-variables

- by default the environment file for Compose (`compose up`, `compose down`) is `.env` located where the command is called
- it can be overridden with `--env-file=./path/to/env`.
- variables declared in the Compose environment file are available in the Compose file

    $ cat .env
    DB_HOST="database"


    $ cat compose.yml
    services:
      app:
        links:
          - "db:$DB_HOST" # set an alias matching the declaration in .env

      db:
        build: postgres

- a specific environment file for a service can be declared with a similar `env_file` attribute

    services:
      app:
        env_file: ./env/app/dev.env

- it can be used along with the Compose env file to set different environment contexts

    $ cat compose.dev.env
    APP_ENV_FILE=app.dev.env

    $ cat compose.yml
    services:
      app:
        env_file: $APP_ENV_FILE


#### The `--env-file` variable

- variables set in the Compose environment file (the default `.env` or specified with `--env-file`) are available in files specified by `env_file`.

    $ cat ./compose.env
    DB_HOST=foo

    $ cat ./app.env
    DBH=$DB_HOST

    $ cat compose.yml
    services:
      app:
        env_file: ./app.env

    $ docker compose --env-file ./compose.env up
