open file
---------

    >>> f = open('x', <modes>) 

modes: 
    r: read
    w: write
    a: append
    
    t: text (default)
    b: binary

# open text file

    >>> f = open('x', 'rt') 
    or 
    >>> f = open('x', 'r') 

# open binary file (e.g. images, pdf)

    >>> f = open('x', 'rb') 


reading from files
------------------

# get all bytes in a string (will move pointer to eof) 

    >>> f.read()

# reset pointer to byte 0, i.e. bof

    >>> f.seek(0)

# list of all lines, from current pointer position to eof

    >>> f.readlines()

# read only 3 first bytes

    >>> f.seek(0)
    >>> f.read(3)


write to files
----------------

# writing to existing file

    >>> f = open('myfile.txt', 'w')
    >>> f.write('my name is michael')
    >>> f.write(' ekoka\n')
    >>> f.close() # required to write in the actual file

# create and write to a new file
                                    
    >>> f = open('myfile.txt', 'w')
    >>> f.writelines(['here is a line,\n', 'and another.\n'])
    >>> f.close() 

# opening file in append mode
                                 
    >>> f = open('myfile.txt', 'a')
    >>> f.write('a multiline file\n')
    >>> f.close()


delete a file
---------------
    >>> os.unlink(path)
    >>> os.remove(path)


rename/move a file
------------------

    >>> os.rename(src, dst)

    # alternatively use
    >>> import shutil
    >>> shutil.move(src, dst)


file meta information 
---------------------
# file name

    >>> f.name


seeking
-------

    # seek 7 bytes from the beginning of file
    >>> f.seek(7, 0)
    
    # seek 7 bytes from current position
    >>> f.seek(7, 1) 
    
    # seek backward 7 bytes from end of file, note the negative sign
    >>> f.seek(-7, 2) 

