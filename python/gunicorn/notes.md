

    sudo /srv/venv/foobarapp/bin/gunicorn \
        --pid /run/gunicorn-foobarapp.pid \
        --bind unix:/run/gunicorn-foobarapp.socket \
        --log-level debug \
        --error-logfile /tmp/foobarapp/gunicorn.error.log \
        --access-logfile /tmp/foobarapp/gunicorn.access.log \
        app:app
