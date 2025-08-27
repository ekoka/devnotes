
### connect to running container as root

    $ sudo docker exec -u 0 -it <CONTAINERID> /bin/bash

or

    $ sudo docker container exec -u root -it <CONTAINERID> /bin/bash

or (with compose) 

    $ sudo docker-compose exec <service> bash
