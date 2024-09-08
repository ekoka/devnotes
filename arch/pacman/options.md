## -b, --dbpath <path>
- specify alternative database location (the default is /var/lib/pacman) 
- don't use unless you know what you're doing
- if specified this is an absolute path

## - r, --root <path>
- specify alternative installation root (default is /)
- should not be used as a way to install software in /usr/local rather than /usr
- if database path or log file are not specified on either the command line or pacman.conf their default location will be inside this root path.
- this option is not suitable for performing operations on a mounted guest system (see --sysroot instead)

## --arch <arch>
specify an alternate architecture

## --cachedir <dir> <dir>
- specify alternate package cache locations
- absolute paths
- defaults to /var/cache/pacman/pkg

## --color <when>
- options are: `always`, `never`, `auto` 
- `auto` enables colors when on a tty

## --config <file>
- specify alternate config file

## --debug
- display debug messages
- enable this option when reporting bugs

## --gpgdir <div>
- specify a directory of files used by GnuPG to verify package signatures
- absolute path
- default is /etc/pacman.d/gnupg
- directory should contain two files: 
    - `pubring.gpg` the public keys of all packagers
    - `trustdb.gpg` the trust database, which specifies that the keys are authentic and trusted

## --hookdir <dir>
- specify alternative 
- default

## -v, --verbose
- output paths such as root, conf file, db path, cache dirs, etc

## --logfile
- specifiy an alternate logfile
- absolute path

## --noconfirm
- bypass all confirmation prompts
- not recommended except for scripts 

## --confirm
- cancels effects of a previous `--noconfirm`

## --sysroot <div>
- specify an alternate system root.
- pacman will chroot and chdir into the system root prior to running.
- allows mounted guest systems to be properly operated on.
- any other paths given will be interpreted as relative to the system root.
- requires root privileges.
