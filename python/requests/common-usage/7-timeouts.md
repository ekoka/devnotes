stop waiting for a response after a set timeout
-----------------------------------------------

    >>> try:
    ...     r = get('http://github.com', timeout=0.001)
    ... except requests.exceptions.Timout as e:
    ...     # skip processing here
    ...     return
    # proceed with processing
