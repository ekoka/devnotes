ref: https://www.postgresql.org/docs/current/arrays.html

## declaration
- append brackets to the data type

    aliases text[]

- can be used in table declaration
    create table user (
        ...
        aliases text[], 
        ...
    )

- multiple dimensions
    
    squares int[][];
    
- declaring size is allowed, but does not inforce it (in postgres)

    -- these are equivalent
    squares int[3][3];
    squares int[][];

- alternative declaration using the `ARRAY` keyword

    -- these are equivalent
    pay_by_quarter int ARRAY[4]
    pay_by_quarter int ARRAY

## array literals 

##### using the `ARRAY` keyword

    ARRAY[1,2];
    ARRAY[[1,2], [3,4]];

##### using a string constant 

- a string of comma separated values surrounded by brackets 
    
    '{john, jill, jane, justine, jeff}';

- multi-dimension

    '{{1,2,3},{4,5,6},{7,8,9}}'
    
- if a value has commas or brackets it must be surrounded by double quotes

    cities text[] =  '{"Montreal, QC", "Toronto, ON", "Vancouver, BC"}';
    range text[] = '{"{3.230 - 7.992}", "{9.283 - 23.023 }"}';

- also use double quotes to include padding (surrounding) spaces
    
    => select 'found' where 'b' = any('{a, b, c}');
    ?column?
    ------
    found
    (1 row)
    
    => select 'found' where 'b' = any('{a, " b", c}');
    ?column?
    ------
    (0 rows)
    
- array string literals are still just strings, they must be converted to arrays first, which some operations such as the above `any()` operator and variable assignment can do implicitly.

        -- e.g. explicit casting
        
        foreach name in ARRAY '{a, b, c}'::text[] loop
            return next name; 
        end loop;
        
        -- or 
        
        foreach name in ARRAY cast('{a, b, c}' as text[]) loop
            return next name; 
        end loop;

## accessing
    
    SELECT name FROM sal_emp 
    WHERE 
        pay_by_quarter[1] <> pay_by_quarter[2];

- by default postgres uses one-based numbering i.e. array of size `n` goes from `[1]` to `[n]`

#### slices 
- accessing arbitrary rectangular slices of an array or subarrays

    SELECT schedule[1:2][1:1] FROM sal_emp WHERE name = 'Bill';
- if any dimension is written as a slice (e.g. `[2:5]`), then all dimensions are treated as slices, and single number dimensions are treated as being from 1 to the number specified.

    e.g. these are equivalent
    schedule[4][2:5]
    schedule[1:4][2:5]
    
- to avoid confusion, it's best to use slice syntax for all dimensions. 
- it's possible to omit upper and lower bound of a slice specifier like `[2:]` and `[:7]`.
