### Add user

    $ sudo useradd

### Create a group

    $ sudo groupadd groupname

### Delete a group

    $ sudo groupdel groupname

### Add user to group

- syntax 

    $ sudo usermod -a -G <group1,group2,...> user

- e.g. add mike to sudo

    $ sudo usermod -a -G sudo,admin mike

- You probably want to use the `-a` option, which stands for "append". If omitted, user is removed from any group not in the list.

### Remove user from group

    $ sudo gpasswd -d user group

### Change user’s primary group

    $ sudo usermod -g groupname username

### Create new user and assign groups in one command

- create user "mike" with primary group "dev" and secondary groups "ops" and "app".

    $ sudo useradd -g dev -G ops,aps mike

### Show user info and groups

    $ id username

- `id` with no username shows info about current user.

    $ id

### Show user's supplementary groups

    $ groups username

- show current user’s groups.

    $ groups



