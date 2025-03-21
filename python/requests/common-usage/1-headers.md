adding headers to a request
---------------------------

    >>> url = 'https://api.github.com/some/endpoint'
    >>> headers = {'user-agent': 'my-app/0.0.1'}
    >>> r = requests.get(url, headers=headers)

authorization
-------------

    >>> auth = ('michael@brazen.ca', '12345pass')
    >>> r = requests.get('https://api.someservice.org/protected/resource', auth=auth)

notes on headers
----------------
- custom headers are given less precedence than more specific source of information. e.g.
    - authorization headers will be overridden if credential are passed with the `auth` param or are specified in a .netrc accessible from the environment.
        
    - authorization headers will be removed if you get redirected off-host. 
    
    - proxy authorization headers will be overridden by proxy credential provided in the url.

    - Content-Length headers will be overridden if the length of content can be determined.

- requests does not change its behavior based on custom headers provided, they are simply passed on into the final request.


