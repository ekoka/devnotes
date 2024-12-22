### references
    https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things
    https://stackoverflow.com/questions/14075581/git-undo-all-uncommitted-or-unsaved-changes
    https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/

### unstage all files you might have staged with `git add`

    $ git reset

### revert all local uncommitted changes (should be executed in repo root)

    $ cd <to repo root>
    $ git checkout .

### revert uncommitted changes only to particular file or directory

    $ git checkout [some_dir|file.txt]

    # longer to type, but works from any subdirectory

    $ git reset --hard HEAD

### remove all local untracked files so only git tracked files remain /!\

    $ git clean -fdx

    /!\ WARNING: -x will also remove all ignored files, including ones specified by .gitignore! You may want to use -n for preview of files to be deleted.

    $ git clean -fdxn
