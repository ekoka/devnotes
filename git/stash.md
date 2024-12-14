Use `git stash` to record current state of working directory and the index, but want to go back to a clean working directory. Local modifications are saved away and working directory is reverted to match the `HEAD` commit.

# to list stashed modifications

    $ git stash list
    
# to inspect stashed modifications

    $ git stash show

# to restore stashed modifications (possibly on top of a different commit)

    $ git stash (apply | pop) [--index] [<stash>]

# to drop stashed modifications

    $ git stash drop

# to stash modifications 
- To save local modifications to a new stash entry and roll back workdir to `HEAD`. 

    // for a quick snapshot
    $ git stash [-p] [<pathspec>...]

    // or to be more specific
    $ git stash push [<push-options>]

### some basic useful push options
- describe stashed state: `-m | --message <message>` 

    $ git stash push --message <message>
    
- interactively select diff patches between `HEAD` and working tree to be stashed with `-p | --patch`. It implies `--keep-index`, but `--no-keep-index` can override this.
    
    $ git stash -p 
    // or 
    $ git stash push -p | --patch 
    
- select which files are stashed with `pathspec` patterns. The index entries and working tree files are then rolled back to the state in `HEAD` only for those. Other files are left intact.

    $ git stash push <pathspec> <pathspec>

- stashing untracked files (but not ignored files): `-u|--include-untracked`
all untracked files are also stashed and then cleaned up with `git clean`, leaving the working directory in a very clean state.

- stashing ignored files (in addition to untracked files): `-a|--all`
both ignored and untracked files are stashed and cleaned 
