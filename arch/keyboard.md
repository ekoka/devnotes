[localectl](https://man.archlinux.org/man/localectl.1)

## Console Keyboard Configuration
- https://wiki.archlinux.org/title/Linux_console/Keyboard_configuration

### The `kbd` package
- a dependency of systemd. 
- provides keyboard mappings, console fonts and console maps 
- also provides low-level tools for managing the text console. 
- In addition, systemd provides the `localectl` tool, which can control both the system locale and keyboard layout settings for both the console and Xorg. 

### List of available keyboard mappings for console
- useful to be used with `localectl set-keymap`

    $ localectl list-keymaps

## setting console key mapping

- Use `loadkeys` to set keymap for current session.

    $ loadkeys keymap

- `loadkeys` is also used internally by `systemd-vconsole-setup` when loading the keymap configured in `/etc/vconsole.conf`.

- A persistent keymap can be set in `/etc/vconsole.conf`, which is read by systemd on start-up. The `KEYMAP` variable is used for specifying the keymap. If the variable is empty or not set, the `us` keymap is used as default value.

- e.g. of `/etc/vconsole.conf`

    KEYMAP=uk

- For convenience, localectl may be used to set the console keymap. It will change the `KEYMAP` variable in `/etc/vconsole.conf` and also set the keymap for the current session.

    $ localectl set-keymap --no-convert <keymap>

- The `--no-convert` option can be used to prevent `localectl` from automatically changing the Xorg keymap to the nearest match.

If required, the keymap from /etc/vconsole.conf can be loaded during early userspace by the keymap mkinitcpio hook.

- Tip:

    If you saved your custom keymap somewhere other than `/usr/share/kbd/keymaps/`, it must be specified by a full path to the file in `vconsole.conf` or when using the `localectl` command above.
    The XKB* variables in `/etc/vconsole.conf` are for Xorg Keyboard configuration. `loadkeys` does not yet support using them; (see kbd issue 72 https://github.com/legionus/kbd/issues/72). And neither does Xorg.

## X11 Keyboard Configuration
- https://wiki.archlinux.org/title/Xorg/Keyboard_configuration

- Can be done many different ways.

### List of layouts, models, variants, or options
- a full list of keyboard layouts, models, variants and options, along with a short description can be found in `/usr/share/X11/xkb/rules/base.lst` 
- for a summary list without a description run

    $ localectl list-x11-keymap-layouts
    $ localectl list-x11-keymap-models
    $ localectl list-x11-keymap-variants
    $ localectl list-x11-keymap-options

### Options
- `XkbModel` 
    - selects keyboard model. 
    - useful only in case your keyboard has some extra keys.
    - for instance laptops with some extra keys that could be made to work by setting an appropriate model. 
    - safe fallbacks are pc104 (ANSI) or pc105 (ISO).

- `XkbLayout` 
    - selects keyboard layout. 
    - Multiple layouts may be specified in a comma-separated list, e.g. us,ca,de

- `XkbVariant` 
    - selects a layout variant available for the `XkbLayout`. 
    - e.g. the default sk (Slovak) variant is qwertz, but you can change it to qwerty, etc.

- `XkbOptions` 
    - extra options (comma-separated). 
    - e.g. layout switching, notification LED, compose mode etc. 
    - See the Frequently used XKB options section for examples.[](https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Frequently_used_XKB_options)

Note: You must specify as many variants as the number of specified layouts. If you want the default variant, specify an empty string as the variant (the comma must stay). For example, to have the default `us` layout as primary and the `dvorak` variant of `us` layout as secondary, specify `us,us` as `XkbLayout` and `,dvorak` as `XkbVariant`.

### Configuration File 
- the syntax of the Xorg file ix explained at https://wiki.archlinux.org/title/Xorg#Configuration
- On Arch for example, you might find the keyboard related config under /etc/X11/xorg.conf.d/00-keyboard.conf

    Section "InputClass"
            Identifier "system-keyboard"
            MatchIsKeyboard "on"
            Option "XkbLayout" "cz,us"
            Option "XkbModel" "pc104"
            Option "XkbVariant" ",dvorak"
            Option "XkbOptions" "grp:win_space_toggle"
    EndSection

### Setting X11 layout with `localectl` (seems problematic with i3 on Arch)
[https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Using_localectl]()

- syntax

    localectl [--no-convert] set-x11-keymap layout [model [variant [options]]]

    # e.g.
    localectl --no-convert set-x11-keymap us,ca grp:alt_shift_toggle

- Configurations will be saved in `/etc/X11/xorg.conf.d/00-keyboard.conf`, this file should not be manually edited, because localectl will overwrite the changes on next start. 

- To set a model, variant or options, all preceding fields need to be specified, but the preceding fields can be skipped by passing an empty string with "".

- Unless the `--no-convert` option is passed, the specified keymap is also converted to the closest matching console keymap and applied to the console configuration in `vconsole.conf`.

- e.g. To create a `/etc/X11/xorg.conf.d/00-keyboard.conf` like the above:

    $ localectl --no-convert set-x11-keymap cz,us pc104 ,dvorak grp:win_space_toggle

- `localectl` additionally writes the keyboard configuration to `/etc/vconsole.conf` using variables `XKBLAYOUT`, `XKBMODEL`, `XKBVARIANT` and `XKBOPTIONS`, [1] but the Xorg server does not read them from that file.

### Setting X11 layout with `setxkbmap`
- See https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Using_setxkbmap

- `setxkbmap` sets keyboard layout for the current X session only
- those settings can be made persistent in `xinitrc` or `xprofile`, which overrides system-wide configuration specified in X configuration files (https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Using_X_configuration_files).

- usage

    $ setxkbmap [-model xkb_model] [-layout xkb_layout] [-variant xkb_variant] [-option xkb_options]

- `setxkbmap` appends options specified in the command line to those previously set (i.e. those saved in the root window properties). 
- To replace all previously set options, use the `-option` flag with an empty argument first.

- To change just the layout (-layout is the default flag):

$ setxkbmap xkb_layout

For multiple customizations:

$ setxkbmap -model pc104 -layout cz,us -variant ,dvorak -option grp:win_space_toggle
    $ setxkbmap -layout "us,ca"
    $ setxkbmap -option "grp:alt_shift_toggle"

- can be added to the i3 config file at `~/.config/i3/config`

    exec "setxkbmap -layout us,ca"
    exec "setxkbmap -option 'grp:shifts_toggle'"
    # or 
    # exec "setxkbmap -option 'grp:alt_shift_toggle'"
    # etc...

- list of available options

    $ localectl list-x11-keymap-options


