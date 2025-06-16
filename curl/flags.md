### Useful flags

##### Info on requests and responses (headers, body, methods, etc)

- `-i, --include` : show response HTTP headers.
- `-I, --head` : fetch the HTTP headers only.
- `-v, --verbose` : view headers and details of request sent by curl.
- `--trace-ascii, --trace <file>` : trace dump of all incoming and outgoing data. Overrides previous use of `-v` or `--trace`. To send output to stdout use `-` as filename.
- `--trace-time` : prepend a time stamp to each trace or verbose line.

Output:

- `-o, --output <file>` : write output to `<file>` instead of stdout. If you're using `[]` or `{}` to fetch multiple docs, use `#` followed by a number in the `<file>` specifier (e.g. `#1`). e.g.

    $ curl http://{one,two}.site.com -o "file_#1.txt"
    $ curl http://{site,host}.host[1-5].com -o "#1_#2.txt"

##### Data

- `-d, --data <data>` : sends specified data in POST request in the same way that a browser does from an HTML form. This will cause curl to pass the data to the server using the content-type application/x-www-form-urlencoded.

Compare to `-F`, `--form`. `-d, --data` is the same as `--data-ascii`. To post data purely binary, instead use the `--data-binary` option. To URL-encode the value of a form field you may use `--data-urlencode`. If any of these options is used more than once on the same  command  line, the data pieces specified will be merged together with a separating &-symbol. Thus, using `-d name=daniel -d skill=lousy` would generate a post  chunk that looks like `name=daniel&skill=lousy`.

If you start the data with the character `@`, the rest should be a file name to read the data from, or `-` if you want curl to read the data from stdin. The contents of the file must already be URL-encoded. Multiple files can also be specified. Posting data from a file named 'foobar' would thus be done with `--data @foobar`.

- `--data-binary <data>` : posts data exactly as specified with no extra processing whatsoever. Data is posted in a similar manner as `--data-ascii` does, except that newlines are preserved and conversions are never done.

- `--data-urlencode <data>` : posts data, similar to the other `--data` options with the exception that this performs URL-encoding.

To be CGI-compliant, the `<data>` part should begin with a name followed by a separator and a content specification. The `<data>` part can be passed to curl using one of the following syntaxes:

    content
        This will make curl URL-encode the content and pass that on.  Just  be careful so
        that the content doesn't contain any = or @ symbols, as that will then make the syntax
        match one of the other cases below!
    =content
        This will make curl URL-encode the content and pass that on. The preceding = symbol is
        not included in the data.
    name=content
        This will make curl URL-encode the content part and pass that on. Note that the name
        part is expected to be URL-encoded already.
    @filename
        This will make curl load data from the given file  (including  any  newlines),
        URL-encode that data and pass it on in the POST.
    name@filename
        This  will  make  curl load data from the given file (including any newlines),
        URL-encode that data and pass it on in the POST. The  name  part gets  an equal sign
        appended, resulting in name=urlencoded-file-content.  Note that the name is expected
        to be URL-encoded already.

- `-F, --form <name=content>` : lets curl emulate a filled-in form. Causes curl to POST data using the "Content-Type: multipart/form-data" according to RFC 2388. This enables uploading of files, etc.

To force the content part in `<name=content>` to be a file, prefix file name with the `@` sign. To just get the content part from a file, prefix with symbol `<`. To read content from stdin instead of file, use `-` as the filename. Works both for `@` and `<`.

    # e.g. send password file to server
    $ curl -F "password=@/etc/passwd" my.server.tld

    # send password file content
    $ curl -F "password=</etc/passwd" my.server.tld

    # type password from command line
    $ curl -F "password=<-" my.server.tld

tell curl what Content-Type to use
    curl -F "web=@index.html;type=text/html" my.server.tld
    or
    curl -F "name=mike;type=text/plain" my.server.tld
change the name field fo a file upload part
    curl -F "file=@localfile;filename=newname" my.server.tld

### Header

- `-H, --header <header>` : Extra header to use when getting a web page.

### tls/ssl:
-1 :
    specify tlsv1
-3 :
    specify sslv3 (aka tlsv1)

--cacert <ca certificate>
    tells curl to use the specified certificate file to verify the peer. File may contain multiple CA certificates and must be in PEM format.
--capath <CA certificates directory>
    tells curl to use the specified certificate directory to verify the peer.


---
http authentification:
-u, --user <user:password>
    curl -1 https

---
Todo:
--url <URL>
    specify a url to fetch.
    mostly handy when specifying URLs in config files.

-X, --request <command>
    specifies custom request method to use.


---
