### Testing a container's DNS

    $ sudo docker run -it <image> bash
    $ ping -c 1 google.com


### Why are there DNS problems in Docker containers
- if Docker can’t find a DNS server defined in the local `/etc/resolv.conf`, containers will default to using Google’s public DNS 8.8.8.8.
- sometimes a network may block access to such public DNS servers to encourage people to use the network’s own DNS server.


### find the DNS server

    $ nmcli dev show | grep 'IP4.DNS'
    IP4.DNS[1]:                             10.0.0.2


### Run the container with the new DNS

    $ sudo docker run --dns 10.0.0.2 <image>



### Set the DNS system wide
- set the DNS settings in `/etc/docker/daemon.json`.

- first, set the local network’s DNS server, and then the Google DNS server as a fall back.

    /etc/docker/daemon.json:
    {
        "dns": ["10.0.0.2", "8.8.8.8"]
    }

- restart the docker service

    $ sudo service docker restart
