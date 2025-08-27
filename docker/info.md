### info on local Docker installation

    $ docker info

### info on container

    $ docker inspect <container_name or ID>

some properties that can be filtered or searched:

    Id
    State
        Status
    Pid
    Image
    Name
    HostConfig
        Binds [ "/home/mike/docker/nginx-project:/var/www/html:ro"]
    PortBindings {
        "80/tcp": [
            {
                HostIp
                HostPort
            }
        ]
    }

    Mounts [
        {
            Source
            Destination
            Mode
            RW
        }

    Config
        Env
    NetworkSettings: {
        Ports: {
            "80/tcp": [
                HostIp
                HostPort
            ]
        }
    }

- find path bindings under: HostConfig > Binds
- find port bindings under: NetworkSettings > Ports
- find PATH under "Config"
