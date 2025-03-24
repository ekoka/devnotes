view response headers
---------------------

    >>> r = requests.get('http://httpbin.org/get')
    >>> r.headers
    {
        ...
        'content-encoding': 'gzip',
        'transfer-encoding': 'chunked',
        'connection': 'close',
        'server': 'nginx/1.0.4',
        ...
    }

- according to RFC 7230 http headers are case insensitive, and this dict complies

    >>> r.headers['content-type']
    'application/json'

    >>> r.headers['Content-Type']
    'application/json'

    >>> r.headers['CoNtEnT-TypE']
    'application/json'

- the different values of a single header field sent multiple times within a single request are concatenated and separated by commas, as specified in RFC 7230

    > A recipient MAY combine multiple header fields with the same field name 
    > into one “field-name: field-value” pair, without changing the semantics 
    > of the message, by appending each subsequent field value to the combined 
    > field value in order, separated by a comma.



