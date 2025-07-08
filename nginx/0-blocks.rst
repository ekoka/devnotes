# nginx blocks
--------------

- configurations are divided logically into hierarchical blocks. Two of whom are of particular interest: `server { ... }` and `location { ... }` .

- server block
    - defines a virtual server to handle specific types of requests.
    - a server block can be assigned to handle a specific domain, port and/or IP address.

- location blocks
    - they live within a server block.
    - they define how nginx should handle requests to specific locations and resources (URIs).
    - useful to subdivide how the uri space should be used.

ref:
https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms
