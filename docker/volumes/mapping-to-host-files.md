- mapping container's `/app` to current working directory

    $ docker run -v $(pwd):/app <image>

- mapping container's `/app` to current working directory, but skip `/app/foo`

    $ docker run -v `/app/foo` -v $(pwd):/app <image>
