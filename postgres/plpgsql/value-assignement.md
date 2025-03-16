## value assignment

    variable := expression;
    or 
    variable = expression;

- the `expression` is evaluated by means of a `SElECT` sent to the database engine.

- the `expression` must yield a single value (possibly a row value)

- the `variable` can be:
    - a simple variable name (optionally qualified with a block name, e.g. `block_name.variable`)
    - a field of a row or record target
    - an element or slice of an array target
    e.g. 
    age := 63;
    user.id := 'AB003443';
    users[3].firstname = 'joe';
    nums[1:3] = array[1,2,3];
- if data types between value and variable don't match, value is coerced. 

