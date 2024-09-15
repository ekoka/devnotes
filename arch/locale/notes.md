https://wiki.archlinux.org/title/Locale

# enabling and setting locale 

- uncomment (enable) a locale in `/etc/locale.gen`

    $ sudo nvim /etc/locale.gen

- generate the enabled locale 
    
    $ sudo locale.gen

- set the locale 

    $ sudo localectl set-locale LANG=fr_CA.UTF-8

    
    
