abs(x)
returns absolute value of a number

>>> abs(-9.2) 
9.2

>>> abs(-3) 
3

>>> abs(2) 
2

---

all(iterable)
returns True if:
    - all elements of `iterable` are true.
    - or if `iterable` is empty.

>>> all([3, 2, 4, 9, 23]) 
True     
>>> all([2, 5, 0, 4]) 
False
>>> all([]) 
True     
>>> all([[]]) 
False
---

any(iterable)

- returns True if any element of iterable is True. 
- If iterable is empty, returns False.

>>> any([False, 0, '', {}, None]) 
False
>>> any([]) 
False
>>> any([False, 0, '', {}, None, 1]) 
True

------

bin(x)
convert an integer to a binary string
>>> bin(3)
'0b11'
>>> bin(15)
'0b01111'
>>> bin(16)
'0b10000'

------
    
callable(object)
- returns True if `object` appears callable, False if not.
- a True return value is not a guarantee that a call to `object` will succeed.
- a False return value guarantees that a call to `object` will fail.

>>> callable(True)
False
>>> callable(lamba: None)
True

------

chr(i)
- returns character at ASCII code `i`
- inverse of `ord()`
>>> chr(97) 
'a'
>>> ord('a')
97

------

classmethod(function)
- returns a class method for function.
- often used as a decorator in class definitions
- note that calss methods and static methods are different. see also `staticmethod()`

class C(object):
    def foo(self):
        print "a string representing our object: {obj}".format(obj=self)
    @classmethod
    def bar(cls):
        print "the name of the class is {name}".format(name=cls.__name__)
    @staticmethod
    def baz():
        print "no argument received here"


------

cmp(x, y)
compares x and y, returns:
    - a positive number if x > y
    - 0 if x == y
    - a negative number if x < y


------
dir() | dir(object)
- dir(): returns the list of names in the current local scope
- dir(object): attempts to return the list of valid attributes for the object
- attribute list returned by dir() is not guaranteed to be accurate, nor consistent across releases.

------
divmod(a, b)
returns a tuple (quotient, remainder) from the division of a by b (a / b)

>>> divmod(5, 2)
(2, 1)
>>> divmod(39, 29)
(1, 10)

------
enumerate(sequence, start=0)
- returns an iterator whose `next()` method returns a tuple of the type (index, item) 
- where the index is initialized with the `start` param.

>>> it = enumerate(['a', 'b', 'c', 'd']) 
>>> it.next()
(0, 'a')
>>> it.next()
(1, 'b')

>>> it = enumerate('abcd', start=4)
>>> it.next()
(4, 'a')
>>> it.next()
(5, 'b')

>>> for k, v in enumerate('abcd', start=-10):
>>>     print (k,v)
(-10, a)
(-9, b)
(-8, c)
(-7, d)

------
execfile(): TODO
------
file(): TODO

------
filter(function, iterable):
- constructs a list from those elements of iterable for which function returns True
- if iterable is a string or a tuple, returns that type, otherwise a list
- see also itertools' iterator versions: ifilter() and ifilterfalse()
- somewhat equivalent to the list comprehension expressions:

    if function is None:
        [item for item in iterable if item]

    if function is not None:
        [item for item in iterable if function(item)]

>>> filter(None, [None, 'a', 'abc', 'xyz', '', {}]) 
['a', 'abc', 'xyz'] 
>>> filter(lambda x: x > 0, (-2, 2, 40, -1, 0, 4, -32))
(2, 40, 4)

------
float([x]): TODO
------
format(value[, format_spec]): TODO
------

frozenset([iterable])
returns a new frozenset object (immutable set).

>>> frozenset('aaabbbccccddddd')
frozenset({'a','b','c','d')

------

getattr(object, name[, default])
returns the value fo the named attribute of object, or default 
------
globals()
- returns a dictionary representing the current global symbol table. 
- within a function, this is the module where it is defined.

------
hasattr(object, name)
- returns True if object has an attribute named name
- name is a string

------
hash(object)
- returns the hash value of the object (if it has one)
- hash value are integer
- used to quickly compare dict keys during dict lookup
- equal numeric values have the same hash value, even if from different types

>>> hash(1) == hash(1.0)

------
help([object]): TODO

------
hex(x)
converts an integer to a hex string

>>> hex(20)
'0x14'

------
id(object)
- returns the identity of an object (integer).
- identity is guaranteed to be unique and constant during an object's lifetime.
- separate objects with non-overlapping lifetimes may have the same identity.
- in CPython, this is the address of the object in memory.

>>> id('abcd')
43715392

>>> id(3)
42025904

>>> id([8,23, 3][2])
42025904

------
input([prompt]):TODO

------
int(x=0)
int(x, base=10) : TODO

------
isinstance(object, classinfo)
- returns True if object is an instance of classinfo, or of a subclass (direct, indirect or virtual)
- classinfo may be a class, a type, or a tuple of classes or types

>>> isinstance(3, int)
True

>>> isinstance('abc', Exception)
False

>>> isinstance('abc', (Exception, str))
True

------
issubclass(class, classinfo)
- returns True if class is a subclass of classinfo (direct, indirect or virtual)
- a class is considered a subclass of itself
- classinfo may be a class, a type, or a tuple of classes or types

>>> issubclass(str, basestring)
True

------
iter(o[, sentinel])
- returns an iterator object
- without sentinel, o must support either the iteration protocol (__iter__()), or the sequence protocol (__getitem__() with integer arguments starting at 0). Otherwise a TypeError is raised.
- with sentinel, o must be callable. The iterator returns the result of o() each time its next() method is invoked. If o()==sentinel, the iterator raises a StopIteration.

>>> it = iter('abc')
>>> it.next()
'a'
>>> it.next()
'b'
>>> it.next()
'c'
>>> it.next()
StopIteration


# StopIteration raised at character 'a'
alpha = list('xyzabcde')
>>> it = iter(lambda:alpha.pop(0), 'a')
>>> for c in it:
...     print c
x
y
z

------
len(s)
- returns the length (number of items) of a object
- s can be string, list, tuple, set, dict 

------
list([iterable]): TODO

------
locals(): TODO
------
long(x=0)
long(x,  base=10): TODO
------
map(function, iterable, ...)
- applies function to every item of iterable and returns a list of the results.
- if there are multiple iterable arguments, function must take that many arguments.
- if one iterable is shorter than the others, it is assumed to be extended with None items.
- if function is None, map uses an identity function (function that simply returns the arguments it's given).
- map is virtually equivalent to list comprehensions (with the zip() function)

    map(function, iterable)
    [function(item) for item in iterable]

- or in case of multiple iterables

    map(function, iterable1, iterable2) 
    [function(x,y) for x,y in zip(iterable1, iterable2)]

- see also filter(), itertools.imap(), itertools.ifilter(), itertools.ifilterfalse()

>>> map(str, [1, 2, 3, 4])
['1', '2', '3', '4']

>>> def concat(x, y, z):
         return ''.join([x,y,z])
>>> map(concat , 'abc', 'def', 'ghi')
['adg', 'beh', 'cfi']

    
------
max(iterable[, key])
max(arg1, arg2, *args[, key])
- returns the largest item in an iterable or from a list of arguments. 
- if one argument is provided, it must be an iterable, and the largest of its items is returned
- if more than one argument are provided, the largest is returned.
- key is a single-argument ordering function, like the one used with sorted() and list.sort(). 
- if supplied, key must be in keyword form: max(a, b, c, key=func)

>>> max('the quick brown fox is on strike') # one argument
'x'

>>> max('axz', 'b', 'c', 'd') # multiple arguments
'd'

>>> winner = max(competitors, key=lambda x: x.score)


------
memoryview(obj): TODO
------
min(iterable[, key])
min(arg1, arg2, *args[, key])
- returns the smallest item in an iterable or from a list of arguments. 
- if one argument is provided, it must be an iterable, and the smallest of its items is returned
- if more than one argument are provided, the smallest is returned.
- key is a single-argument ordering function, like the one used with sorted() and list.sort(). 
- if supplied, key must be in keyword form: min(a, b, c, key=func)

>>> min('the quick brown fox is on strike') # one argument
' '

>>> min('axz', 'b', 'c', 'd') # multiple arguments
'axz'

>>> loser = min(competitors, key=lambda x: x.score)

------
next(iterator[, default])
- retrieves the next item from iterator by calling its next() method
- if default is given, it is returned if the iterator is exhausted, otherwise a StopIteration is raised

>>> it = iter('xyz')
>>> next(it)
'x'
>>> next(it)
'y'
>>> next(it)
'z'
>>> next(it)
StopIteration
>>> next(it, 'EOF')
'EOF'

------
object()
- return a new featureles object.
- object is a base for all new style classes

>>> o = object()

>>> d = {o: 'abc'}
>>> d[o]
'abc'

>>> class C(object):
        pass

------
oct(x)
- converts an integer to an octal (base-8) string

>>> oct(8)
'010'

>>> oct(15)
'017'

------
open(name[, mode[, buffering]]): TODO
- prefered method of opening a file. 
- returns file type object.
- if file can't be open, IOError is raised.
- mode is a string indicating how the file is to be opened. 
- common mode values:
    - 'r': read, IOError if doesn't exist (default)
    - 'r+': read and write, IOerror if doesn't exist.
    - 'w': open or create file for writing. truncate existing content.
    - 'w+': truncate or create file for reading and writing. truncate existing content.
    - 'a': open or create file for writing. append to existing content. 
    - 'a+': open or create file for reading and writing. append to existing content.

------
ord(c):
- c must be a string of length one.
- if c is a unicode string (of length one), returns the unicode code point (in decimal).
- if c is an 8 bit character, returns the byte value.

>>> ord('a')
97

>>> ord(u'\u00e9')
233

>>> ord(u'é')
233


------
pow(x, y[, z])
- without z, returns x to the power y. equivalent to x**y
- if z is present, return x to the power y, modulo z
- if z is present, x and y must be integer and y must be non-negative

>>> pow(2, 3)
8

>>> pow(2, -3)
0.125

------
------
------
reduce(function, iterable[, initializer])
- returns a single value, computed by cumulating calls to a 2 argument function, on items of iterable, from left to right.
- on the first call to function, the first argument is either the initializer, if provided, or the first item in the iterable. The second item is the following item in the iterator (which is still the first item if initializer is present).
- on subsequent calls to function, the first argument is the result of the last call, and the second is the next item from the iterable.

>>> def add(x,y):
        return x+y
>>> reduce(add, [1,2,3,4])
10

