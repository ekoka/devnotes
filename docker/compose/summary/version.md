https://docs.docker.com/compose/compose-file/compose-versioning/

- there are 3 legacy versions of the Compose file format: 1, 2.x, and 3.x, with 1 being deprecated since June 2023.
- to specify version 1, omit the `version` declaration at the root of the document.
- if using version 2, specify it.

- The latest and recommended version of the Compose file format is documented in the [compose specification](https://docs.docker.com/compose/compose-file/).

- Several things may differ depending on which version is used
    - The structure and permitted configuration keys
    - The minimum Docker Engine version that must be running
    - Compose's behaviour with regards to networking

These differences are explained [here](https://docs.docker.com/compose/compose-file/compose-versioning/).

### `version` according to the [Compose specification](https://github.com/compose-spec/compose-spec/blob/master/04-version-and-name.md)
- The top-level `version` property is defined by the Compose Specification for backward compatibility. It is only informative.
- Compose doesn't use `version` to select an exact schema to validate the Compose file, but prefers the most recent schema when it's implemented.
- Compose validates whether it can fully parse the Compose file. If some fields are unknown, typically because the Compose file was written with fields defined by a newer version of the Specification, you'll receive a warning message. Compose offers options to ignore unknown fields (as defined by "loose" mode).
