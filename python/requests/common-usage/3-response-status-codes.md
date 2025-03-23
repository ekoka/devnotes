check the response status code
------------------------------

    >>> r = requests.get('http://httpbin.org/get')
    >>> r.status_code
    200

status code lookup
------------------

    >>> r.status_code == requests.code.ok
    True

raising error in case of bad status
-----------------------------------

    >>> r = requests.get('http://httpbin.org/get/some/inexisting/url')
    >>> r.status_code
    404

    >>> r.raise_for_status()
    Traceback (most recent call last):
        File "requests/models.py", line 832, in raise_for_status 
            raise http_error 
    requests.exceptions.HTTPError: 404 Client Error

    # when status_code is 200 `raises_for_status()` does nothing
    >>> r = requests.get('http://httpbin.org')
    >>> r.status_code
    200
    >>> r.raise_for_status()
    None

    # e.g. pattern

    >>> try:
    ...     r = requests.get(url)
    ...     r.raise_for_status()
    ... except requests.exceptions.HTTPError as e:
    ...     # skip processing of request
    ...     return
    ... # process request starting here
