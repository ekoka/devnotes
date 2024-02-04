# config file location

    $ pip config -v list

Will list the paths that pip searches for config. There are different paths for 'global', 'user', 'site' and you can specify your own.
    
    $ pip config debug

Will list the paths and tell whether they exist or not.

# config for pip running in virtualenv
    
    ~/.virtualenvs/myproject/pip.conf
