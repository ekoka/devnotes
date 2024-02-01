##### ref: https://packaging.python.org/en/latest/tutorials/packaging-projects/

### Create `pyproject.toml`

- `pyproject.toml` tells "frontend" tools like *pip* and *build* what "backend" tool to use to create distribution packages for the project (e.g. Hatchling, setuptools, Flit, PDM).


    # pyproject.toml using hatchling

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"


    # pyproject.toml using Flit

    [build-system]
    requires = ["flit_core>=3.4"]
    build-backend = "flit_core.buildapi"


- `requires`: a list of packages that are needed to build your package. Build frontends like *pip* install them automatically in a temporary, isolated virtual environment for use during the build process.
- `build-backend`: the name of the Python object that frontends will use to perform the build.


### Configure metadata

    # pyproject.toml

    ...

    [project]
    name = "example_package_ekoka"
    version = "0.0.1"
    authors = [
        {name="Michael Ekoka", email="michael@sundry.ca"}
    ]
    description = "A small example package"
    readme = "README.md"
    requires-python = ">=3.7"
    classifiers = [
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

    [project.urls]
    "Homepage" = "https://github.com/pypa/sampleproject"
    "Bug Tracker" = "https://github.com/pypa/sampleproject/issues"

- `name`:  the *distribution name* of the package. Can be anything, but limited to `[a-zA-Z0-9._-]`.

- `version`: the package version. See PEP 440 https://peps.python.org/pep-0440/.

- `classifiers`:
    - gives the index and pip some additional metadata about the package.
    - See https://pypi.org/classifiers/.
    - include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on.

- The project metadata specification:
https://packaging.python.org/en/latest/specifications/declaring-project-metadata
https://packaging.python.org/en/latest/specifications/core-metadata

### Add a `README.md` file

### Add a `LICENSE` file
- it's important for every package uploaded to PyPI to include a license. See https://choosealicense.com/
- most build backend automatically include license files in packages.

### Other files
- the files listed above will be included automatically in the source distribution.
- to include additional files, consult the build backend's documentation.

### Generating distribution archives (e.g. `build`)
- install the latest version of `build` (you may need to `sudo apt install python3-venv` prior).

    $ python3 -m pip install --upgrade build

- from the same directory the `pyproject.toml` file is located, run

    $ python3 -m build

- two files should be generated inside a `dist` directory

    example_package_ekoka-0.0.1.tar.gz
    example_package_ekoka-0.0.1-py3-none-any.whl

- the `.tar.gz` is a *source distribution*
- the `.whl` is a *built distribution*

- Newer `pip` version prefer built distributions, but will fall back to source if needed.
- Always upload a source distribution and provide built distributions for the platform your project is compatible with.

### Uploading to PyPI
- register an account on PyPI and get an API token
