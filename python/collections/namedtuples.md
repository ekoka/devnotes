
### syntax

- signature

    # returning a new tuple subclass named `typename`
    namedtuple(typename, field_names[, verbose=False][, rename=False])

    # e.g.
    Point = namedtuple('Point', 'x y')

- if `rename` is true, invalid fieldnames are automatically replaced with positional names. For example, `['abc', 'def', 'ghi', 'abc']` is converted to `['abc', '_1', 'ghi', '_3']`, eliminating the keyword `def` and the duplicate fieldname `abc`.
- if `verbose` is true, the class definition is printed just before being built.

- The `field_names` are a sequence of strings such as `['x', 'y']` or  a single string with each `fieldname` separated by whitespace and/or commas, for example `'x y'` or `'x, y'`.

### fieldname
- can contain letters, digits, and underscores.
- cannot start with a digit or underscore. 
- cannot be a *keyword* (e.g. `class`, `for`, `return`, `global`, `pass`, `print`).

### namedtuple properties
- fields accessible by *attribute lookup* as well as being *indexable* and *iterable*. 
- instances do not have per-instance dictionaries, so they are lightweight and require no more memory than regular tuples.
