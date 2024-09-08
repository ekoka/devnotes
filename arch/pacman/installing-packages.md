## package
- An archive containing:
    - all compiled files of application
    - metadata about application, such as app name, version, dependencies, etc
    - installation files and directives for pacman 
    - (optionally) extra files to make your life easier (e.g. start/stop script)

- advantages to using a package manager over compiling yourself
    - easy updates
    - dependency check, installation, and handling
    - clean removal, no files unintentionally left behind


- when installing a package only required as an optional dependency of some other package (i.e. otherwise not required by you), it is recommended to use the `--asdeps` option. 

## installing specific packages

    - a list of packages
    # pacman -S package_1 package_2 ...

    - a list of packages with regex
    # pacman -S $(pacman -Ssq package_regex)

## refresh the package database

    # pacman -Sy
