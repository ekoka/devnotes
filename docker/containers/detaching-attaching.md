##### https://stackoverflow.com/questions/25267372/correct-way-to-detach-from-a-container-without-stopping-it

### detach from container (without stopping)
- `ctrl-p ctrl-q` works if started with `-it`
- `ctrl-c` works if started with `-t` (without `-i`)
- detaching by killing the `docker.*attach` process

    # from another shell window
    $ ps -ef | grep attach
    $ kill -9 <docker.attach PID>

    # or

    $


### configure detach key combination
- config file

    # ~/.docker/config.json

- key combos

    # e.g. detach by pressing "Ctrl-b", followed by "x"
    {
        "detachKeys": "Ctrl-d,x"
    }

- supported keys (can be used in conjunction with `ctrl-` or standalone).

    a-z
    @
    _
    [
    \\ : two backslashes
    ^

### reattach

    $ docker attach <container>

    # connect all streams except stdin
    $ docker attach --no-stdin <container>

- the shell's `$?` variable is set, so it's possible to inspect the container's exit code
