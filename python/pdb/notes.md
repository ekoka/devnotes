ref: https://realpython.com/python-debugging-pdb/

### Invoke the debugger

- importing and running

    import pdb; pdb.set_trace()

- in python 3.7+

    breakpoint()

- by running pdb as a python module and passing a file

    $ python -m pdb app.py arg1 arg2


### Printing and evaluating code

- print the whole source for the current function or frame with `ll` (longlist)

    (Pdb) ll 
       7 def some_function():
       8     """this is a some function"
       9     foo = 'bar'
      10     return foo + 'baz'

- to see a short snippet of code use `l`

- print a variable or evaluate code with `p`

    (Pdb) p foo + 'baz'
    barbaz

- use `pp` for pretty-printing, useful for structured data


### Stepping through code
- commands

    n(ext) : continue execution until the next line in the current function is reached or it returns
    s(tep) : execute current line and stop at the first possible occasion (either in a function that is called or in the current function)

### Breakpoints

- set a breakpoint with the `b(break)` command

    b(reak) [ ([filename:]lineno | function) [, condition] ]

    # the `condition` argument is very powerful, it allows to specify a Python expression that, when evaluating to true, will cause pdb to break. 

    # breakpoint using the source filename and file number

        (Pdb) b util:5

    # breakpoint using function name

        (Pdb) b util:get_path

    # breakpoint with a condition
        
        (Pdb) b util.get_path, not filename.startswith('/')

- list all breakpoints with `b` without arguments

    (pdb) b
    Num Type        Disp    Enb     Where 
    1   breakpoint  keep    yes     at /code/util.py:1

- enable/disable breakpoints  with `enable bpnumber` and `disable bpnumber`

    
    (Pdb) disable 1
    Disabled breakpoint 1 at /code/util.py:1
    (Pdb) b
    Num Type        Disp    Enb     Where 
    1   breakpoint  keep    no      at /code/util.py:1
    (Pdb) enabled 1
    Enabled breakpoint 1 at /code/util.py:1
    (Pdb) b
    Num Type        Disp    Enb     Where 
    1   breakpoint  keep    yes      at /code/util.py:1

- delete a breakpoint with `cl(ear)`

    (Pdb) clear filename:lineno
    (Pdb) clear [bpnumber [bpnumber...]]
