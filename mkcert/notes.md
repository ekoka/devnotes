### Development HTTPS with `mkcert`
`mkcert` is a utility that allows to create local certs for SSL. This can be useful in development. See: https://github.com/FiloSottile/mkcert for details on how to install and create wildcard certs (if you haven't done so already).

    $ mkcert -install
    Created a new local CA
    The local CA is now installed in the system trust store!
    The local CA is now installed in the Firefox trust store (requires browser restart)!

    $ mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1

    Created a new certificate valid for the following names
    - "example.com"
    - "*.example.com"
    - "example.test"
    - "localhost"
    - "127.0.0.1"
    - "::1"

    The certificate is at "./example.com+5.pem" and the key at "./example.com+5-key.pem"


Once the cert and its corresponding key have been created, point to them in the server's config file.

    # config.py

    HTTP_SCHEME = 'https'
    HOST = 'my-development-server.local'
    HTTP_PORT = 8989
    HOST_WITH_PORT = "%s:%s" % (HOST, HTTP_PORT)
    SSL_CONTEXT = (
        '/path/to/example.com+5.pem',
        '/path/to/example.com+5-key.pem',
    )

##### Connecting to local https with Python's Requests
If you have some problems with Requests unable to read the SSL certificate emitted with the responses, it's because Requests is not configured to read the local machine's root certs by default, but its own. See:
- https://stackoverflow.com/questions/42982143/python-requests-how-to-use-system-ca-certificates-debian-ubuntu
- https://stackoverflow.com/questions/46604114/python-requests-ssl-error-certificate-verify-failed
- https://github.com/FiloSottile/mkcert/issues/49

As suggested in one of the proposed solutions, you can export an environment variable to point Requests to the proper root cert.

    $ export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
    # no spaces here ----------^

    # or
    $ export REQUESTS_CA_BUNDLE=$(mkcert -CAROOT)/rootCA.pem
