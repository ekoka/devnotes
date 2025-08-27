### passing environment variables

    sudo docker run -it -e FOO="quick fox" --env BAR=lazy dog" <image> bash

### passing contents of .env file

- passing the contents of .env into a variable to be expanded inside the container can help when docker is capricious with env vars.

    sudo docker run -it --env ENV_FILE="$(cat ./.env)" <image> bash

- The app is then launched with a shell script that first exposes the content of `$ENV_FILE`

    #!/bin/bash

    set -a; source <(printf '%s' "$ENV_FILE" ); set +a;
    # or, if you're in bash you can also use echo
    set -a; source <(echo -n "$ENV_FILE" ); set +a;

    python app.py

### passing environment variables with `--env-file`
