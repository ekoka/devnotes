- all exceptions raised by requests inherit from requests.exceptions.RequestException

network problem errors (DNS failures, refused connections, etc)
---------------------------------------------------------------

    try:
        r = requests.get('http://somewebsite.net')
    except requests.exceptions.ConnectionError as e:
        # handle ConnectionError here
    

invalid HTTP response 
---------------------

    try:
        r = requests.get('http://somewebsite.net')
    except requests.exceptions.HTTPError as e:
        # handle HTTPError here


timeout exception
-----------------

    try:
        r = requests.get('http://somewebsite.net', timeout=0.05)
    except requests.exceptions.Timeout as e:
        # handle Timeout here


request exceeds configured number of redirects
----------------------------------------------

    try:
        r = requests.get('http://somewebsite.net')
    except requests.exceptions.TooManyRedirects as e:
        # handle TooManyRedirects here
