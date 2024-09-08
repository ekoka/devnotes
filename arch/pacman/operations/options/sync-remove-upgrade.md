### -d, --nodeps
- skip dependency version checks
- package names are still checked
- pacman will always check a package's dependency fields to ensure all dependencies are installed
- specify this option twice to skip all dependency checks

### --assume-installed <package=version>
- add a virtual package with version "version" to the transaction to satisfy dependencies 
- allows to disable specific dependency checks without affecting all dependency checks

### --dbonly
- adds/removes database  entry only, leaving all files in place

### --noprogressbar
- do not show progress bar when downloading files
- useful for scripts that call pacman and capture the output

### --noscriptlet
- if an install scriptlet exists, do not execute it
- avoid this option unless you know what you're doing

### -P, --print
- only print the targets instead of performing the actual operation
- use `--print-format` to specify how targets are displayed

### --print-format <format>
- specify a printf-like format
