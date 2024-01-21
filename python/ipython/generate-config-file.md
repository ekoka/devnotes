
    $ ipython profile create

- then in the config file, create the `c.InteractiveShellApp.exec_lines` list 

    # e.g. ~/.ipython/profile_default/ipython_config.py

    c = get_config()
    c.InteractiveShellApp.exec_lines = []
    c.InteractiveShellApp.extensions = []
    
    # add autolreoad instructions
    c.InteractiveShellApp.extensions.append('autoreload')
    c.InteractiveShellApp.exec_lines.append('%autoreload 2') 

    
