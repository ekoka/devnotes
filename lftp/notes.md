# syntax
lftp [-d] [-e cmd] [-p port] [-u user[,pass]] [site]
lftp -f script_file
lftp -c commands
lftp --version
lftp --help

# options
-d : switch debugging mode
-e commands : execute given commands and don't exit
-p port : use given port to connect
-u user[,pass] : 
-c commands : execute given commands and exit. commans can be separated with `;`, `&&` or `||`. option must be used alone without other arguments.

# open a connection and specify the method to use (http, ftp, sftp, ftps, etc)

    open http://www.us.kernel.org/pub/linux

# move job: 
    - to background: c-z 
    - to foreground: `wait` or `fg`

# list jobs: `jobs`

# mirror directory tree: 
    download: mirror
    upload: mirror -R

# launch a job at specified time in current context: `at`

# queue commands for sequential execution for current server: `queue <cmd>`

commands
--------
!<cmd> : shell commands on local host
    !ls
    !cd

    # note that when issuing a local command in an lftp script
    # you need to issue an `exit` command to revert back to the lftp prompt.

alias [name [value]] : define or undefine alias name
    alias dir ls -lF
    alias less more
    alias less # undefine

at <time> [-- command] : wait until given time to execute command
    

command <cmd> [args...] : execute given command ignoring aliases
    

debug [-o file] level|off : set debugging level and optional file to redirect output

    
# eval [-f format] args
    e.g.
    # no format given. executes a normal mirror.
    eval queue mirror remotedir localdir
    # this format specifies a reverse mirror.
    eval "$0 -R $2 $1" queue mirror remotedir localdir

# exit [bg] [top] [kill] [code] (see man page)

# fg : alias for `wait`

# open [-e cmd] [-u user[,pass]] [-p port] host|url

# source <file> | source -e <command> : execute commands recorded in file or returned by specified external command

    source ~/.lftp/rc
    source -e cat ~/.lftp/rc 


