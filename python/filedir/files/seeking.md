
### `s.seek()` syntax

    f.seek(offset, [whence])

### using `whence`
- indicates the relative positioning of the seeking
- possible values are: 

    0 or os.SEEK_SET # absolute file positioning (default)
    1 or os.SEEK_CUR # relative to the current position
    2 or os.SEEK_END # relative to the file's end

- it's probably better to use the constants

    # ok
    f.seek(5, 0)   
    f.seek(5, 1)
    f.seek(-5, 2)
    
    # better
    import os
    f.seek(5, os.SEEK_SET)   
    f.seek(5, os.SEEK_CUR)
    f.seek(-5, os.SEEK_END)

### Examples

- move 5 bytes from the beginning

    f.seek(5, os.SEEK_SET)

- move to the beginning

    f.seek(0, os.SEEK_SET)

- move 5 bytes from the end

    f.seek(-5, os.SEEK_END)

- move to the end

    f.seek(0, os.SEEK_END)

- move 5 bytes after the current position

    f.seek(5, os.SEEK_CUR)

- move to the current position

    f.seek(0, os.SEEK_CUR)

- move 5 bytes before the current position

    f.seek(-5, os.SEEK_CUR)
