difference between `root` and `alias`
-------------------------------------

- consider the two location configuration structures

    # location1
    location <prefix> {
        root <root>;
    }

    # location2
    location <prefix> {
        alias <alias>;
    }

- given a request GET /some/url/to/a/resource

- and these two location configurations

    # location1 (with root)
    location /some/url {
        root /var/www/mysite
    }

    # location2 (with alias)
    location /some/url {
        alias /var/www/mysite
    }

    such that: prefix = "/some/url"


- location1 (with root) will append the entire url path to the `root` to find the resource:
    
    root             url path
    /var/www/mysite  /some/url/to/a/resource

    resource
    /var/www/mysite/some/url/to/a/resource
        
- second location only appends the part coming _after_ the prefix to the `alias`
    
    alias            [prefix]   path
    /var/www/mysite  [/some/url]/to/a/resource

    resource
    /var/www/mysite/to/a/resource

- one can achieve somewhat of the same convenience offered by `alias` with `root` using a rewrite

    location /some/url {
        root /var/www/mysite
        rewrite ^/some/url(.*) $1 break;
    }
        

- when the prefix is just a '/' character, one should be careful when specifying an alias since the resolution only takes the part coming *after* the prefix.

    # for e.g.

        location / {
            alias /my/image/dump
        }

    # if a request comes in as:

        GET /cute-kitten.jpg

    # the resource is resolved as

        [alias] + [url path minus the prefix]

    # or 

        /my/image/dump + cute-kitten.jpg        =>       /my/image/dumpcutekitten.jpg 

    # which will likely not resolve to what's expected

    # for the same reason a request to the index path

        GET /

    # might not produce what's expected

        /my/image/dump + (empty-string)         =>      /my/image/dump 

    # which, because it doesn't end with a slash will be considered a file (that doesn't exist) and the server will unsuccessfuly try to return it, resulting in a 404.

    # if (1) the prefix ends with a slash and (2) the alias maps to a directory, it's better to stay consistent and specify the latter with a trailing slash to minimize unpredictable behavior.
 
