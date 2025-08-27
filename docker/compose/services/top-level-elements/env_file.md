### `env_file` services top-level option
- adds environment variable to container based on file content.

    # single file
    env_file: .env

    # list of files
    env_file:
      - ./a.env
      - ./b.env

    # list as mapping, to set `required` attribute
    env_file:
      - path: ./default.env
        required: true # default
      - path: ./override.env
        required: false

##### format
- see format https://docs.docker.com/compose/compose-file/05-services/#env_file-format
- Each line must be in `VAR[=[VAL]]` format.
- Unquoted and double-quoted (") values have Interpolation applied.
- Each line represents a key-value pair. Values can optionally be quoted.

        VAR=VAL     -> VAL
        VAR="VAL"   -> VAL
        VAR='VAL'   -> VAL

- Inline comments for unquoted values must be preceded with a space.

        VAR=VAL # comment           -> VAL
        VAR=VAL# not a comment      -> VAL# not a comment

- Inline comments for quoted values must follow the closing quote.

        VAR="VAL # not a comment"   -> VAL # not a comment
        VAR="VAL" # comment         -> VAL

- Single-quoted (') values are used literally.

        VAR='$OTHER'        -> $OTHER
        VAR='${OTHER}'      -> ${OTHER}

- Quotes can be escaped with \.

        VAR='Let\'s go!'                -> Let's go!
        VAR="{\"hello\": \"json\"}"     -> {"hello": "json"}

- Common shell escape sequences including \n, \r, \t, and \\ are supported in double-quoted values.

        VAR="some\tvalue"       -> some value
        VAR='some\tvalue'       -> some\tvalue
        VAR=some\tvalue         -> some\tvalue

- `VAL` may be omitted, in such cases the variable value is an empty string. `=VAL` may be omitted, in such cases the variable is unset.
