location blocks
---------------

- syntax

    location <modifier> location_match {
        ...
    }

- location_match:
    - defines what nginx should check the url against.

- `modifier`
    - presence or absence of `modifier` affects how nginx attempts to match the location.
        - no modifier: location is interpreted as a prefix match. ie the location given will be matched against the beginning of the request uri.
        - `=` (equal sign) modifier : request uri must match location exactly.
        - `~` (tilde) modifier : location is interpreted as a case-sensitive regex match.
        - `~*` (tilde and asterisk) modifier: case-insensitive regex match.
        - `^~` (caret and tilde): non-regex match that disable other regex match attempts if it is determined to be the best non-regex match (see selection algorithm for explanation).

    ---
    e.g. prefix match
    location /site {
        ...
    }
    valid for URIs
        /site
        /site/page1/index.html
        /site/index.html
    
    ---
    e.g. exact match
    location = /page1 {
        ...
    }
    valid for URI /page1
    invalid for 
        /site/page1
        /page1/index.html

    ---
    e.g. case-sensitive regex match
    location ~ \.(jpe?g|png|gif|ico)$ { 
        ...
    }
    valid for URIs
        /cat.jpg
        /assets/logo.ico
    invalid for 
        /cat.JPG

    ---
    e.g. case-insensitive regex match
    location ~* \.(jpe?g|png|gif|ico)$ { 
        ...
    }
    valid for URIs
        /cat.jpg
        /cat.JPG

    ---
    e.g. non-regex match that disables subsequent regex match attempts (see selection algorithm for explanation)
    location ^~ /images {
        ...
    }
    valid for URIs
        /images/cats.jpg

- location selection algorithm
    1) check prefix-based location matches, i.e. non-regex matches.
        a) search exact matches: (location using the `=` modifier). The first exact match is selected and the search ends.
        b) non-exact prefix: if no exact match is found, nginx search for the longest matching prefix.
            - if the longest matching prefix uses the `^~` modifier, the search ends and the location is selected.
            - else the match is stored by nginx for the moment.
    2) after the longest matching prefix is determined and stored nginx evaluates regex locations (both case sensitive and insensitive). locations are evaluated sequentially. the first match is immediately selected to serve the request.
    3) if no regex location is matched to the request uri, the previously stored prefix is location is selected.

    * Note that nginx prioritize regex matches over prefix matches, but allows to override this preference with the `=` and `^~` modifiers.
    * Also note that prefix matches are prioritize based on the longest match, regex are prioritized based on the first match.
