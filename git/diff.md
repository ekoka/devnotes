### help

    $ git diff --help
    
or
    
    $ man git-diff
    
### syntax
    
    git diff [<options>] [<commit>] [--] [<path>...]
    git diff [<options>] --cached [<commit>] [--] [<path>...]
    git diff [<options>] <commit> <commit> [--] [<path>...]
    git diff [<options>] <blob> <blob>
    git diff [<options>] --no-index [--] <path> <path>


### examples
- see the diff between the `HEAD` (currently checked out commit) and other commit of a file 

    # syntax
    $ git diff  <commit>    [HEAD]  <filepath>

    # command
    $ git diff  b7d8b92c            ./path/to/scripts/file.js

### some interesting options

    -p, -u, --patch : generate patch (default)
    -s, --no-patch  : suppress diff output
    --ouptut=<file> : output to file instead of stdout

