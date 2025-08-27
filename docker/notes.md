- the recommended way to configure the docker daemon flags and environment variables is to use the platform independent `/etc/docker/daemon.json`
- one thing that is not configurable with dameon.json is a HTTP proxy.
- if using Upstart or SysVinit to manage the docker daemon, the default config can be set in `/etc/default/docker`. Note, as stated in the file, that this does not apply to SystemD.

### DNS issues

ref: https://stackoverflow.com/questions/24991136/docker-build-could-not-resolve-archive-ubuntu-com-apt-get-fails-to-install-a
- first check that it's not a docker connectivity issue

    # ping OpenDNS (208.67.222.222 or 208.67.220.220)
    # or Cloudflare (1.1.1.1 or 1.0.0.1)
    # or Google (8.8.8.8 or 8.8.4.4)
    # or DNSResolver(205.210.42.205 or 64.68.200.200)
    $ docker run --rm busybox ping -c 1 1.1.1.1

- if that's fine, identify primary and secondary DNS set in the system

    $ nmcli dev show | grep 'IP4.DNS'

- set them in the /etc/docker/daemon.json file

    {
        "dns": ["208.67.222.222", "208.67.220.220"]
    }

- restart the docker daemon

    $ sudo systemctl restart docker


#### data-only container

pattern was to allow data to be shared among multiple containers

- the port mapping in docker-compose is between the network and a container Foo, not between other containers and Foo.

    containers <-> [ network ] <-> public-port <-> [mapping] <-private-port-> Foo Container

- it allows other containers to call Foo by its name without specifying its public port.
- Ensure the container's configuration files abide.

- you can connect to the container from outside compose, by using its public port.
