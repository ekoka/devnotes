#!/bin/sh

## as seen here: https://nickjanetakis.com/blog/dealing-with-lock-files-when-using-ruby-node-and-elixir-with-docker

set -e

built_lock_file="/tmp/Gemfile.lock"
current_lock_file="Gemfile.lock"

function cp_built_lock_file() {
    cp "${built_lock_file}" "${current_lock_file}"
}

if [ -f "${current_lock_file}" ]; then
    diff="$(diff "${built_lock_file}" "${current_lock_file}")"
    if [ "${diff}" != "" 2>/dev/null ]; then
        cp_built_lock_file
    fi
else
    cp_built_lock_file
fi

exec "$@"
