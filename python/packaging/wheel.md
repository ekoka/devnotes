See: https://packaging.python.org/en/latest/specifications/binary-distribution-format/

- Originally defined in PEP 427

- A wheel is a ZIP-format archive with a specially formatted file name and the `.whl` extension.
- it contains a single distribution nearly as it would be installed according to PEP 376 with a particular installation scheme.

- although a specialized installer is recommended, a wheel file may be installed by simply unpacking into the `site-packages` with the standard `unzip` tool, while preserving enough information to spread its contents out into their final paths at any later time.

- wheels provide a simpler interface (than the previous sdist approach). The format frees installers from being aware of the build system, or to need to install it in the target environment.

### E.g. installing `distribution-1.0-py32-none-any.whl`
There are two phases:
-  unpacking
    1. parse `distribution-1.0.dist-info/WHEEL`
    2. verify that installer is compatible with wheel version. Warn if minor version is greater. Abort if major version is greater.
    3. if `Root-is-Purelib == 'true'`, unpack archive into purelib (directory for site-specific, non-platform specific files).
    4. Else unpack into platlib (directory for site-specific, platform-specific files).

- spreading
    1. Unpacked archive includes `distribution-1.0.dist-info/` and (if there is data) `distribution-1.0.data/`.
    2. Move each subtree of `distribution-1.0.data/` onto its destination path. Each subdirectory of `distribution-1.0.data/` is a key into a dict of destination directories, such as `distribution-1.0.data/(purelib|platlib|headers|scripts|data)`. The initially supported paths are taken from `distutils.command.install`.
    3. If applicable, update scripts starting with #!python to point to the correct interpreter.
    4. Update distribution-1.0.dist-info/RECORD with the installed paths.
    5. Remove empty distribution-1.0.data directory.
    6. Compile any installed .py to .pyc. (Uninstallers should be smart enough to remove .pyc even if it is not mentioned in RECORD.)
