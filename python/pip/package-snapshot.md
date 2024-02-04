# taking a snapshot of currently installed packages
- all packages

    $ pip freeze

- packages in a virtualenv, as well as globally installed ones 

    # first activate virtualenv
    $ workon env1
    (env1)$ pip freeze

- only packages in virtualenv, ignoring gloabl ones 
    
    (env1)$ pip freeze -l
    # saving the list
    (env1)$ pip freeze -l > dependencies.txt

- installing from a dependency list

    (env1)$ pip install -r dependencies.txt
    

