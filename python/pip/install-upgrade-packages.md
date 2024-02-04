
# installing a python packages

- latest stable version

    $ pip install somepackage

- a specific version

    $ pip install somepackage==1.5.3

- inside the ~/.local/ directory

    $ pip install --user somepackage

- prior to installing packages with pip on Ubuntu ensure that python-dev and setuptools are installed

    $ sudo apt-get install python-dev python-setuptools

- installing from a requirement list

    (env1)$ pip install -r requirement.txt

# upgrading:

- to latest stable version

    $ pip install somepackage --upgrade

- upgrading/downgrading to a specific version

    $ pip install somepackage==1.3.8 --upgrade


# installing from version control repository
- over http

    $ pip install hg+http://url/to/hg-repository#egg=packagename
    $ pip install git+http://url/to/git-repository#egg=packagename
    $ pip install svn+http://url/to/hg-repository#egg=packagename

- local file system

    $ pip install hg+file:///path/to/local/repository

- over git protocol

    $ pip install git+git://url/to/git-repository#egg=packagename


# install only in virtualenv

- set the environment variable `PIP_REQUIRE_VIRTUALENV=1` to enforce pip installing packages only in an active virtualenv.

Or put

    [install]
    require-virtualenv = true

    [uninstall]
    require-virtualenv = true

into the pip config file.

- disable it when installing Python versions using something like asdf or there will be errors about not finding virtualenv.
