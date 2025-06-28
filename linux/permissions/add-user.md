
## `useradd` syntax

    $ sudo useradd [OPTIONS] username

- creates user based on OPTIONS on command line and default values in `/etc/default/useradd`.

- also reads the content of `/etc/login.defs` file.

    # e.g.
    $ sudo useradd mike

- adds an entry to /etc/passwd, /etc/shadow, /etc/group, and /etc/gshadow.

- verify that user was created and view details with `id` command

    $ sudo id mike

- to log in as newly created user, you need to set the user password.

    $ sudo passwd mike

- add new user and create home directory with `-m | --create-home` to set user home as `/home/<username>`

    sudo useradd -m mike

- initialization files are copied from from `/etc/skel/` to home directory. If you list the files in the /home/jane directory

    $ ls -la /home/mike/

    total 20
    drwxr-x--- 2 jane jane 4096 Dec 20 17:58 .
    drwxr-xr-x 4 root root 4096 Dec 20 17:58 ..
    -rw-r--r-- 1 jane jane  220 Jan  6  2022 .bash_logout
    -rw-r--r-- 1 jane jane 3771 Jan  6  2022 .bashrc
    -rw-r--r-- 1 jane jane  807 Jan  6  2022 .profile

## create user with custom home location with `-d |--home` 


    $ sudo useradd -m -d /opt/mike mike

## creating a User with a Specific User ID

In Linux and Unix-like operating systems, users are identified by unique UID and username.

User identifier (UID) is a unique positive integer the Linux system assigns to each user. The UID and other access control policies are used to determine the types of actions a user can perform on system resources.

By default, when a new user is created, the system assigns the next available UID from the range of user IDs specified in the login.defs file.

Invoke the useradd command with the -u (--uid) option to create a user with a specific UID.

For instance, to create a new user named jane with a UID of 1500, you would type:

sudo useradd -u 1500 jane

You can verify the user’s UID, using the id command:

id -u jane

1500

Creating a User with a Specific Group ID

Linux groups are organization units that are used to organize and administer user accounts in Linux. The primary purpose of groups is to define a set of privileges, such as reading, writing, or executing permission for a given resource that can be shared among the users within the group.

When creating a new user, the default behavior of the useradd command is to create a group with the same name as the username and the same GID as the UID.

The -g (--gid) option allows you to create a user with a specific initial login group. You can specify either the group name or the GID number. The group name or GID must already exist.

The following example shows how to create a new user named jane and set the login group to users:

sudo useradd -g users jane

To verify the user’s GID, use the id command:

id -gn jane

users

Creating a User and Assign Multiple Groups

There are two types of groups in Linux operating systems: Primary and Secondary (or supplementary) groupss. Each user can belong to exactly one primary group and zero or more secondary groups.

You can use the -G (--groups) option to specify a list of additional (supplementary) groups for the user.

The following command creates a new user named john with primary group users and secondary groups wheel and docker.

sudo useradd -g users -G wheel,docker john

You can check the user groups by typing:

id john

uid=1002(john) gid=100(users) groups=100(users),10(wheel),993(docker)

Creating a User with a Specific Login Shell

When a new user is created, its login shell is set to the one specified in the /etc/default/useradd file. In some distributions, the default shell is set to /bin/sh, while in others, it is set to /bin/bash.

The -s (--shell) option allows you to specify the new user’s login shell.

Here’s an example showing how to create a new user named john with /usr/bin/zsh as a login shell type:

sudo useradd -s /usr/bin/zsh john

Check the user entry in the /etc/passwd file to verify the user’s login shell:

grep john /etc/passwd

john:x :1001:1001::/home/john:/usr/bin/zsh

Creating a User with a Custom Comment

The user’s full name or contact information can be added as a comment.

To add a short description for the new user use the -c (--comment) option.

In the following example, we are creating a new user named john with the text string “Test User Account” as a comment:

sudo useradd -c "Test User Account" john

The comment is saved in /etc/passwd file:

grep john /etc/passwd

john:x :1001:1001:Test User Account:/home/john:/bin/sh

The comment field is also known as GECOS.
Creating a User with an Expiry Date

To define a time at which the new user accounts will expire, use the -e (--expiredate) option. This is useful for creating temporary accounts.

The date must be specified using the YYYY-MM-DD format.

For example, to create a new user account named john with an expiry time set to January 22, 2025 you would run the following:

sudo useradd -e 2025-01-22 john

Use the chage command to verify the user account expiry date:

sudo chage -l john

The output will look something like this:

Last password change					: Dec 11, 2023
Password expires					: never
Password inactive					: never
Account expires						: Jan 22, 2025
Minimum number of days between password change		: 0
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7

Creating a System User

System users are typically created during OS and package installations, and there is no real technical difference between them and regular users.

Use the -r (--system) option to create a system user account. For example, to create a new system user named john you would type:

sudo useradd -r john

System users are created with no expiry date. Their UIDs are chosen from the range of system user IDs specified in the login.defs file, which is different than the range used for regular users.
Changing the Default useradd Values

The default useradd options can be viewed and changed using the -D, --defaults option or by manually editing the /etc/default/useradd file.

To view the current default options, type:

useradd -D

The output will look something like this:

GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
CREATE_MAIL_SPOOL=no

Let’s say you want to change the default login shell from /bin/sh to /bin/bash. To do that, specify the new shell as shown below:

sudo useradd -D -s /bin/bash

You can verify that the default shell is changed by running the following command:

sudo useradd -D | grep -i shell

SHELL=/bin/bash

