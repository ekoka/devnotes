import requests module
-------------------------

    >>> import requests

response object
---------------

    # GET, POST, PUT, etc
    >>> r = requests.get('https://api.github.com/events')
    >>> r = requests.post('http://httpbin.org/post')
    >>> r = requests.put("http://httpbin.org/put")
    >>> r = requests.delete("http://httpbin.org/delete")
    >>> r = requests.head("http://httpbin.org/get")
    >>> r = requests.options("http://httpbin.org/get")

query string params
-------------------

    >>> params = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get('http://httpbin.org/get', params=params)
    >>> print(r.url)
    http://httpbin.org/get?key1=value1&key2=value2

    # list of items
    >>> params = {'key1': 'value1', 'key2': ['value2', 'value3']}
    >>> r = requests.get('http://httpbin.org/get', params=params)
    >>> print(r.url)
    http://httpbin.org/get?key1=value1&key2=value2&key2=value3

response content
----------------

    >>> r = requests.get('https://api.github.com/events')
    
    # text content
    >>> print(r.text)
    u'[{"repository": {"open_issues": 0, "url": "https://github.com/...'

response encoding
-----------------

    # reading
    >>> r.encoding
    'utf-8'

    # changing
    >>> r.encoding = 'ISO-8859-1'

- if you change the encoding request will use the value in `r.encoding` whenever you call `r.text`.

binary response content
-----------------------

    >>> r.content
    b'[{"repository": {"open_issues": 0, "url": "https://github.com/...'

- `deflate` and `gzip` transfer-encoding are automatically decoded
- e.g. create an image from image content transfered

    >>> from PIL import Image
    >>> from StringIO import StringIO
    >>> r = requests.get('https://imageapi.io/somepic.jpg')
    >>> i = Image.open(StringIO(r.content))
