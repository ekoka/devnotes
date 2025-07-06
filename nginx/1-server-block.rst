server blocks
-------------

    server {
        ...
    }

# which server block will handle the request
- 2 directives used within server blocks to select them: `listen` and `server_name`

    server {
        listen 122.33.5.33:80;
        server_name api.example.com;
    }
    

- listen: 
    - typically defines which IP address and port the server block responds to.
    - if not defined defaults to 0.0.0.0:80 (or 0.0.0.0:8080 if nginx is being run by a non-root user). It allows the server block to respond to any interface on port 80, although this default value holds a lower priority on the server selection process.  
    - can be set to :
        - IP:port combo
        - IP without port (defaults to port 80)
        - port without IP (which listens to every interface on that specific port)
        - path to a unix socket (usually used to pass requests between different servers)

    - selection process:
        - a block with no `listen` defaults to 0.0.0.0:80
        - a block set to 155.155.155.155 with no port becomes 155.155.155.155:80
        - a block set to port 8888 with no IP, becomes 0.0.0.0:8888

        - nginx then attempt to collect a list of blocks that match the request most specifically, based IP and port. That is any block using 0.0.0.0 will not be selected if there are other blocks specifically matching the requested IP. In any case the port must be matched exactly.
        - if only one most specific match is found, that server is used to serve the request.
        - if multiple server blocks with the same specificity level, nginx then evaluates their `server_name` directive.
        - /!\ Note that the `server_name` is *only* evaluated to differentiate between two server blocks whose `listen` directives qualify them for a request in IP, port and priority.

            e.g. if example.com is hosted on 192.168.1.10, although the second block's `server_name` qualifies it for requests on example.com, the first block has higher priority on the `listen` directive and will therefore always be selected:

            server {
                listen 192.168.1.10; # defaults to 192.168.1.10:80
                ...
            }

            server {
                listen 80; # defaults to 0.0.0.0:80
                server_name example.com;
            }

            - request: GET example.com/some/location
            - translates to 192.168.1.10:80/some/location
            - matches both blocks, but first block is more specific and thus has higher priority, it's therefore selected.


- server_name
    - evaluated when multiple servers qualify for a request by their `listen` directive (in IP, port and specificity).
    - nginx checks the request's "Host" header which holds the domain or IP address that the client was trying to reach.
    - server_name to Host matching sequence: 
        1) exact match: find `server_name` that match Host exactly. If multiple exact matches found, use first one.
        2) leading wildcard match: if no exact match found in (1), find a leading wildcard match (indicated by a * at the beginning of the server_name). If multiple matches found, select the longest match.
        3) trailing wildcard match: if no leading wildcard match found in (2), find a trailing wildcard match (indicated by a server_name ending with *). If multiple matches found, select the longest match.
        4) regex match: if no trailing wildcard match found in (3), evaluates server_name defined as a regex (indicated by a ~ before the server_name). The *first* whose server_name regex matches is selected.
        5) default server: if no regex match found in (4), default server block for IP address and port is used. 
            - each IP:port combo has a default server block that will be used when a course of action can not be determined. 
            - for an IP:port combo this will be either the first block in the configuration or the block containing the `default_server` option as part of the `listen` directive (which would override the first-found algorithm).
            - there can be only one default_server declaration per IP:port combo.

    e.g. Host = hosts1.example.com
    server {
        listen 80;
        server_name *.example.com;
        ...
    }
    server {
        listen 80;
        server_name host1.example.com; # <- exact match selection 
        ...
    }

    ---

    e.g. Host = www.example.org
    server {
        listen 80;
        server_name www.example.*;
        ...
    }
    server {
        listen 80;
        server_name *.example.org; # <- longest leading match selection
        ...
    }
    server {
        listen 80;
        server_name *.org;
        ...
    }

    ---

    e.g. Host = www.example.com
    server {
        listen 80;
        server_name host1.example.com;
        ...
    }
    server {
        listen 80;
        server_name example.com;
        ...
    }
    server {
        listen 80;
        server_name www.example.*; # <- longest trailing match selection
        ...
    }

    ---

    e.g. Host = www.example.com
    server {
        listen 80;
        server_name example.com;
        ...
    }
    server {
        listen 80;
        server_name ~^(www.|host1).*\.example\.com$; # <- first regex match selection
        ...
    }
    server {
        listen 80;
        server_name ~^(subdomain|set|www|host1).*\.example\.com$;
        ...
    }


ref:
https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms

