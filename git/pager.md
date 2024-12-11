### prevent git to send output to pager

    $ git --no-pager <command> [command options]

e.g. git log

    $ git --no-pager log -n 10

- to disable diff's pager by default

    $ git config pager.diff false

- set git's pager to cat for all commands

    $ git config --global core.pager cat

### setting pager's app
- cat

    # one offs
    $ git diff | cat

    # with colors
    $ git diff --color | cat

    # configured
    $ git config --global core.pager cat

- less

    $ git config --global core.pager "less -FRSX"
    - immediately quit if the diff fits on the first screen (-F)
    - outputs raw control characters (-R)
    - chops long lines rather than wrapping (-S)
    - do not use termcap init/deinit strings (-X)
