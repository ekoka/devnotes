## -T, --deptest
- check dependencies

    # pacman -T deps1 deps2...

    e.g. check if qt and bash>=3.2 are present
    # pacman -T qt "bash>=3.2"

- will check each dep specified and return a list of deps not currently satisfied
- useful in scripts (such as `makepkg`) to check installed packages
- accepts no other options

