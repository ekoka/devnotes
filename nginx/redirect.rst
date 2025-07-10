- a new location search can be triggered by certain directives within a selected location
- some directives of interest:
    - index
    - try_files
    - rewrite
    - error_page

---

- index: a directive that always specifies an internal redirect
    - if you make an exact location match that is a directory and has an `index` directive specified, there's a good chance that the request will be redirected to a different location. 

    - e.g. consider these two locations 

        location = /exact_match {
            index index.html;
            ...
        }

        location / {
            ...
        }
        
        - if /exact_match is a match for a directory, its index directive will trigger an internal redirect to /exact_match/index.html, which will then not honor the exact match requirement of the first location.
        - the subsequent location although not optimal is then a match.
        - to limit the execution in the first block, you need to find a different method to satisfy a request to the directory.
            e.g. you could set an invalid index for the block and turn on autoindex.

            location = /exact_match {
                index nothing_will_match;
                autoindex on;
                ...
            }

- try_files: a directive that tells nginx to check for the existence of a named set of files or directories. The last parameter can be an uri that nginx will make an internal redirect to.
    
    - e.g. consider a request for /blahblah and the following 2 locations

        root /var/www/main;
        location / {
            try_files $uri $uri.html $uri/ /fallback/index.html;
        }

        location /fallback {
            root /var/www/another;
        }

        - nginx will search subsequently for:
            /var/www/main/blahblah
            /var/www/main/blahblah.html
            /var/www/main/blahblah/
        - failing in all 3 attempts it will redirect to /fallback/index.html
        - the redirect will trigger a new location search that will match the second location block
        - second block attempts to serve the file /var/www/another/fallback/index.html
            
- rewrite: 
    - ref: http://nginx.org/en/docs/http/ngx_http_rewrite_module.html#rewrite
    - syntax
        rewrite <regex> <replacement> [flag];

    - match a uri based on <regex> and replace it with <replacement>

    - `rewrite` directives are executed sequentially in order of appearance in the config file.

    - further processing can be terminated by using a <flag>.
        - `last` : stop processing the current set of ngx_http_rewrite_module directives (break, if, return, rewrite, set) and begin a search for a new matching location.
        - `break`: stops processing the current set of ngx_http_rewrite_module directives, but proceed with other processing.
        - `redirect`: returns a temporary redirect with code 302; used if a replacement sring does not start with "http://" or "https://".
        - `permanent`: returns a permanent redirect with code 301.

    - if <replacement> starts with "http://" or "https://" the processing stops and a redirect is returned to the client.

    - the full redirect url is formed according to the request scheme ($scheme) and the `server_name_in_redirect` directive (defaults to off) and the `port_in_redirect` (defaults to on) directive. When `server_name_in_redirect` is disabled the name of the "Host" request header field is used instead, if the field is not present the IP address of the server is used.

    - the query string in the <regex> part of the directive are not modified in the <replacement>. They are appended at the end of the <replacement>. To prevent this add a '?' character at the end of the <replacement>.

        e.g. rewrite ^/users/(.*)$ /show?user=$1? last

    - if a <regex> includes the '{' or ';' characters it should be enclosed in single or double quotes.

    - e.g. consider the request GET /rewriteme/pets/cat.jpg which will be redirected from the first to the second location block

        root /var/www/main;
        
        location / {
            rewrite ^/rewriteme/(.*)$ /$1 last;
            ...
        }

        location /pets {
            ...
        }

- error_page: 
    - can lead to an internal redirect similar to `try_files`
    - used to define what should happen when certain status codes are encountered.
    - e.g. internal redirect to /another/whoops.html in case of 404 status code.
        root /var/www/main;
        
        location / {
            error_page 404 /another/whoops.html;
            ...
        }

        location /another {
            root /var/www;
            ...
        }

