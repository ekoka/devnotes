- `image` can be used to specify the container's base image preexisting image

    services:
      redis:
        image: redis:alpine

- `build` can be used instead or in addition, to point to a Dockerfile, or a build context (that contains a Dockerfile).

- `build` specifies the build configuration for creating a container image from source, as defined in the [Compose Build Specification](https://docs.docker.com/compose/compose-file/build/).

- `build` can be a context path or a detailed build definition

#### `build` as context path
- can be absolute or relative.
    - if relative, it is resolved from the build context, usually the Compose file's parent folder, unless specified otherwise with the `context` attribute.
    - if absolute, it prevents the Compose file from being portable, so a warning is displayed.
- the path is used as a context to execute the build
- a canonical Dockerfile is looked for at the root of the directory.

        # e.g. to point to the ./webapp directory as the build config context for an image

        services:
          app:
            build: ./webapp
              ports:
                - "8000:5000"
              environment:
                FLASK_DEBUG: "true"

#### `build` as detailed definition
- build arguments can be specified,
- including an alternate Dockerfile location, which can be absolute or relative.
    - if relative, it is resolved from the `compose.yml` file's parent folder.
    - if absolute, it prevents the Compose file from being portable, so a warning is displayed.


### `build` and `image` attributes
- when both are used, rules of the service's `pull_policy` attribute apply.
- If `pull_policy` is missing, Compose tries to pull the image first from registry or cache. Then if not found, it's built from source.
`pull_policy` defines the decisions Compose makes when it starts to pull images. Possible values are:
    - `always`: always pulls image from registry.
    - `never`: doesn't pull image from registry. Relies on cached image, else reports failure.
    - `missing`: pulls image only if not available in cache. Default option if you're not also using the Compose Build Specification. `if_not_present` is considered an alias for this value for backward compatibility.
    - `build`: builds the image. Rebuilds if already present.

    service:
      app:
        image: ...
        build: ...
        pull_policy: missing

### `build` attributes

ref: https://docs.docker.com/compose/compose-file/build/#attributes

---

### Base image (Build)

    version: '3.3'
    services:
        app:
            container_name: website
            restart: always
            build: .
            ports:
                - '3000:3000'
        command:
            - 'npm run start'

In this example, we define our images using the build tag which takes the destination of our Dockerfile as a parameter.

The last option of defining the base image is to use a Dockerfile with a custom name.

build:
    context: ./dir
    dockerfile: Dockerfile.dev
