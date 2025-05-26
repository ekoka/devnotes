
### install

    $ docker pull postgres


### run

    $ docker run \
    --name pg_foobar \
    –-rm \
    -e POSTGRES_USER=foobar POSTGRES_PASSWORD=1234abcd \
    -d
    -v ${PWD}/data:/var/lib/postgresql/data \
    -p 5433:5432 \
    postgres

- Initialization of database is skipped if directory already contains a database. This includes the creation of `POSTGRES_USER`.

### flags

    --rm :  remove the container when it's stopped
    -e POSTGRES_PASSWORD=<password> : mandatory env variable for admin user
    -d : detached mode: allows container to run in the background  ### connect

### connect interactively

    $ docker exec -it pg_foobar bash

### connect from host (e.g. using psql on default port 5432)

    # restoring database from dump file
    $ psql -U foobar -h localhost -p 5433 < foobar.sql

- When restoring from a dump without specifying the database, it is inferred from the name of the user (i.e. its default db, in this case `foobar`).
