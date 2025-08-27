
    services:
      app:
        restart: always # ("no", on-failure, unless-stopped)
        ...

- note that in yml `no` is equivalent to `false` so you have to use the string `"no"`.

- restart only on failure

    services:
      app:
        restart: on-failure # with exit code other than 0
        ...
