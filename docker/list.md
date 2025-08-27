### listing containers

- list all running containers

    $ docker ps

- list all containers, running or not, with `a` flag

    $ docker ps -a

- show only containers' numeric ID with `q` flag

    $ docker ps -aq

- filter containers to list based on specific condition

    $ docker ps -aq -f status=exited
