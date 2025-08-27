
### override image's default command and start an interactive shell

    $ sudo docker run -it <image> /bin/bash
    # or
    $ sudo docker run -it <image> bash

### Set dns

    $ sudo docker run -it --dns 8.8.8.8 <image> bash


### passing environment variables in .env file

- passing the entire .env content to a variable because docker cli is notoriously unreliable with env vars

    sudo docker run -it --env ENV_FILE="$(cat ./.env)" <image> bash

- The app is then launched with a shell script that first exposes the content of `$ENV_FILE`

    #!/bin/bash

    set -a; source <(printf '%s' "$ENV_FILE" ); set +a;
    # or, if you're in bash you can also use echo
    set -a; source <(echo -n "$ENV_FILE" ); set +a;

    python app.py

### connecting ports

    sudo docker run -it -p 8989:5000 <image> bash

### Connect to local host

    sudo docker run -it --add-host host.docker.internal:host-gateway <image> bash
