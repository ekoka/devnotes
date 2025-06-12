
### the problem with `-print`
- `-print` outputs the full file name on the standard output, followed by a newline.
- Sometimes you need to pipe the output to another program that uses empty spaces to delimit files. 
- if no file name in the list contains such space characters, the list provided by `-print` expectedly has each file name separated by newlines. The other program will accurately parse each file name.
- however if a file name contains empty space characters (newline, tabs, spaces), the other program should be directed to use something other than empty spaces to successfully parse the file name.
- `-print` can't be configured to end file names with something else than a newline. 
- if piping to another program from `find`,  use `-print0` instead of `-print`

### `-print0` as an alternative to `-print`
- like `-print`, it outputs the full file name on the standard output, but it follows it by a  null character, instead the newline.
- program that process the output can thus be configured to split the output by the null character and file names can contain white space. For instance with `xargs`, `-0` is the corresponding option.


- e.g. list all files under the current tree whose name contains "foobar", and change their permission to `644`
    
    $ find . -name "*foobar*" -type f -print0 | xargs -0 chmod 644
