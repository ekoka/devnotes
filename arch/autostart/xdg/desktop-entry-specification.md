# Desktop Entry Specification

- ref: https://specifications.freedesktop.org/desktop-entry-spec/latest/index.html

- both KDE and GNOME have adopted a similar format for "desktop entries" or config files describing how a particular program is to be launched, how it appears in menus, etc.

## File naming
- should have the `.desktop` extension, except for files of type `Directory`, which should have the `.directory` extension. Determining file type based on extension is quick and easy. Withou extension present, the desktop system falls back to "magic detection".

- for apps, the part of the name of the desktop file before the `.desktop` extension should be a valid `D-Bus` well-known name (i.e. a sequence of [A-Za-z0-9-\_] characters separated by dots and not starting with a number).

- should follow the "reverse DNS" convention, starting with a reverse DNS domain name controlled by the author of the application, written in lower case. Domain name should be followed by CamelCase name (by convention) of application.  e.g. if owner of "example.org" is author of "Foo Viewer", they might choose `org.example.FooViewer.desktop`.

- dashes are not allowed because of potential conflicts. Replacing them with underscore is recommended.

- if name starts with digit, prepend with an underscore. e.g. "7-zip.org" -> "org.\_7\_zip.Archiver.desktop"

### Desktop File ID 
- each desktop entry that represent an application is identified by its `.dekstop file ID`, which is based on its filename.

- To determine the ID of a desktop file, make its full path relative to its `$XDG_DATA_DIRS` component in which the desktop file is installed, remove the "application/" prefix and replace '/' with '-'.

    e.g. /usr/share/applications/foo/bar.desktop -> foo-bar.desktop

- if the desktop file is not installed in an `applications/` subdir of one of the `$XDG_DATA_DIRS` components, it does not have an ID.
