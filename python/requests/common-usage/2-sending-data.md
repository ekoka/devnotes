form-encoded data (like html forms)
-----------------------------------
- simply pass a dict to the `data` param and it will be form-encoded
    >>> data = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.post('http://httpbin.org/post', data=data)
    >>> print(r.text)
    {
        ...
        "form": {
            "key1": "value1",
            "key2": "value2"
        },
        ...
    }

non-form-encoded data (e.g. some general textual data)
------------------------------------------------------
- simply pass a string to the `data` param (as opposed to a dict as described above)
    # e.g. sending some json data
    >>> import json
    >>> data = json.dumps({'key1': 'value1', 'key2': 'value2'})
    >>> r = requests.post('http://httpbin.org/post', data=data)


json-encoded data
-----------------
- although it's possible to encode the data in json yourself as described for non-form-encoded data above, it's simpler to use the `json` param with a dict

    >>> data = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.post('http://httpbin.org/post', json=data)

multipart-encoded files
-----------------------

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file'=open('report.xls', 'rb')}
    >>> r = request.post(url, files=files)
    >>> r.text
    {
    ...
        "files": {
            "file": <censored...binary...data>
        },
    ...
    }

- setting the `filename`, `headers` and `content_type` explicitly for each file

    >>> filename = 'report.xls'
    >>> filecontent = open('report.xls', 'rb')
    >>> file_content_type = 'application/vnd.ms-excel'
    >>> file_headers = {'expires': '0'}
    >>> report = (filename, filecontent, file_content_type, file_headers)
    >>> files = {'report': report}
    >>> r = request.post(url, files=files)

- sending a string to be received as a file

    >>> usercontent = 'firstname,lastname,email\nmichael,ekoka,michael@brazen.ca'
    >>> userfile = ('user.csv', usercontent)
    >>> files = {'user': userfile}
    >>> r = request.post(url, files=files)

- sending a very large file by streaming the data (see requests.toolbelt in advanced documentation)

- sending multiple files in a single request (see advanced documentation)
