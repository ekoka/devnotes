- create a bare *staging* repository on the server

    $ mkdir -p /srv/repos/foo/staging.git
    $ cd /srv/repos/foo/staging.git
    $ git init --bare

- create a hook to automate push to deployment directory

    $ cd hooks
    # create the file 'post-receive' with execute permission
    $ vim post-receive

        #!/bin/sh
        git --work-tree=/srv/www/foo.staging --git-dir=/srv/repos/foo/staging.git checkout -f

    $ chmod +x post-receive

- from the local repository add the bare remote repository

    $ git remote add staging ssh://mike@remote/srv/repos/foo/staging.git

- now pushing from the local repository to the *staging* server will trigger the `post-receive` hook

    $ git push staging master

- to push to a *live* directory we can repeat some of the steps

    $ mkdir -p /srv/repos/foo/live.git
    $ cd /srv/repos/foo/live.git/hooks
    $ vim post-receive

        #!/bin/sh
        git --work-tree=/srv/www/foo.live --git-dir=/srv/repos/foo/live.git checkout -f

    # add bare live as remote for staging bare
    $ cd /srv/repos/foo/staging.git
    $ git remote add live /srv/repos/foo/live.git
    # now pushing to the live from staging will update the live work tree copy
    $ git push live master
