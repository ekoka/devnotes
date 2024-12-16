Ref: https://stackoverflow.com/a/40272289/56974

- There are situations where files have been added to a Git repository, but you want Git to stop tracking them for changes in your own working copy.
- Examples of this are vendored libraries (i.e. libraries that you've included a copy of right along your own code and committed to the repository).
- It's sometimes necessary to tell Git to stop tracking such files because they might change in non-obvious, but potentially problematic ways, such as permission changes.
- You can tell Git to stop tracking the files for change in your own copy, *without* removing them from the repository. 

# Only tracked files 
- Note that you can only tell git to stop tracking files that it's already tracking.
- So first, ensure that the file you want to skip is being tracked.
- you can use the `git ls-file` utilities to list tracked or untracked files.
    
Listing tracked files under the ".../foobar/" tree
    
    $ git ls-files path/to/foobar/
    aaa.py
    ...
    zzz.py

Confirming that a specific file is tracked

    $ git ls-files path/to/foobar/aaa.py
    path/to/foobar/aaa.py

Listing currently untracked files under the ".../foobar/" tree

    $ git ls-files -o ./path/to/foobar/
    .settings.conf
    aaa.pyc
    ...
    zzz.pyc

Confirming that a specific file is currently untracked

    $ git ls-files -o app/sdk/settings.conf
    app/sdk/settings.conf

Listing ".gitignored" files under a tree that match a `<pattern>`
    
    $ git ls-files -o -i -x <pattern> <tree>
    e.g.
    $ git ls-files -o -i -x "*.pyc" ./path/to/foobar/

# `--skip-worktree` vs `--assume-unchanged` 
- ref: https://stackoverflow.com/questions/13630849/git-difference-between-assume-unchanged-and-skip-worktree

- there are two subcommands to `git update-index` you can use to ask git to stop tracking files locally:
- `--assume-unchanged` is a promise by the user that the local files will not change. The bit is reset if the remote's version of the file has changed. This is primarily to avoid expensive file checks.
- `--skip-worktree` instructs git to never touch a file, regardless of whether there's a new remote version of it, or it's been locally modified and is more actual than remote's.
- there are "undo" version of the above commands, just prefix them with `--no-` as in `--no-assume-unchaged` and `--no-skip-worktree`.

# Only works with files
- `git update-index` only work on file paths not directory paths, since git doesn't really care about directories.
- to make it recursive, you must use list the files you want to skip and pipe the list to `git update-index`:
- e.g. find all files and symlink under the "foo/bar/" tree and mark them for skipping

    $ find foo/bar/ -type f,l -print0 | xargs -0 git update-index --skip-worktree


# 1) keep local files, but delete them from the repo 
- i.e. anyone else that pulls the repo won't see them. 


    git rm --cached <file-name> 
    
or 
    
    git rm -r --cached <folder-name>

add files to `.gitignore`

# 2) Stop tracking files that never change or only change insignificantly (e.g. permissions)
- e.g. SDKs that probably won't ever change. 
- tells Git to stop checking that huge folder every time for changes, locally, since it won't have any. 
- The `assume-unchanged` index will be reset and file(s) overwritten if there are upstream changes to the file/folder (when you pull).

    git update-index --assume-unchanged <path-name>

# 3) have your own independent version of the file or folder
- e.g. you don't want to overwrite (or delete) production/staging config files.

    git update-index --skip-worktree <path-name>

- the command does not propagate with Git. Users have to run it independently.
    
---
Note that to undo either #2 or #3, you can use the `[no-]` variant of the respective commands:

    git update-index --no-assume-unchanged <path-name>

    git update-index --no-skip-worktree <path-name>
