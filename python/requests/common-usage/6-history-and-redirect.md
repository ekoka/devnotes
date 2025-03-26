- by default requests automatically performs all redirection for all verbs except HEAD

tracking redirections with `Response.history`
---------------------------------------------
    >>> r = requests.get('http://github.com')
    >>> r.url
    'https://github.com/'
    >>> r.history
    [<Response [302]>, <Response [301]>]


disable redirections in GET, PUT, PATCH, POST, DELETE, OPTIONS
--------------------------------------------------------------

    >>> r = requests.get('http://github.com', allow_redirects=False)

enable redirections in HEAD
---------------------------

    >>> r = requests.get('http://github.com', allow_redirects=True)
