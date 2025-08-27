

Syntax

    $ docker build -t <namespace>/<project[:tag]> <build context>

e.g.

    $ docker build -t ekomic/liteb2b:latest .

When running

    $ docker run ekomic/liteb2b[:latest]

The process is called tagging, but technically only the portion after the colon is the tag.
