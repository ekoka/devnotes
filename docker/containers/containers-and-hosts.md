### ref
- https://stackoverflow.com/a/24326540/56974
- https://stackoverflow.com/questions/24319662
- https://docs.docker.com/engine/reference/run/#network-host

### connecting to localhost

    # make host accessible through 'host.docker.internal'
    $ sudo docker run --add-host host.docker.internal:host-gateway <image>

- `--add-host` adds an entry to the container's `/etc/hosts` file and maps `host.docker.internal` to the container's host gateway. The value `host.docker.internal` can be replaced with a different one.

### using docker's default bridge
- docker creates a bridge named `docker0` by default. Both the docker host and containers have an IP address on that bridge.

    $ sudo docker run --network="bridge" <image>

- you can find the host or container's IP by querying their `ip addr` command


    # look for the "global" scope IP address
    $ ip addr show docker0
    3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
        link/ether 02:42:bc:68:f3:0c brd ff:ff:ff:ff:ff:ff
     -> inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
        valid_lft forever preferred_lft forever
        inet6 fe80::42:bcff:fe68:f30c/64 scope link
        valid_lft forever preferred_lft forever

    # thus the host's (or container's) IP address on the bridge is 172.17.0.1

### host as container's localhost
- add `--network=host`

    $ sudo docker -d run --network=host <image>

- now from within container you can connect to localhost or 127.0.0.1.

- with docker-compose

    services:
        myapp:
            network_mode: host
