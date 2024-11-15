ref: https://www.postgresql.org/docs/14/rowtypes.html

- represent the structure of a row or record.
- essentially just a list of field names and their data types.
- can be used in many of the same ways that simple types are used.
- syntax comparable to `CREATE TABLE`, but only field names and types.

## Declaration 

    CREATE TYPE inventory_item AS (
        name            text,
        supplier_id     integer,
        price           numeric
    );

- can then be used to create tables or functions

    -- table
    CREATE TABLE on_hand (
        item    inventory_item,
        count   integer
    );

    INSERT INTO on_hand
    VALUES (ROW('fuzzy dice', 42, 1.99), 1000);

    -- function
    CREATE FUNCTION price_extension(inventory_item, integer) 
    RETURNS numeric
    AS $$
        SELECT $1.price * $2
    $$ LANGUAGE SQL

## Composite types and tables
- whenever a table is created a composite type with the same name is automatically also created to represent the table's row type

- note however that since no constraints are associated with a composite type, the constraints of the table definition *do not apply* to values of the composite type outside the table. 

- to circumvent this, you can create a domain over the composite type, and apply the desired constraints as `CHECK` constraints of the domain.

## composite values as literal constants
- syntax

    '(val1,val2,...)'

- values can be surrounded by quotes, which they must if containing commas or parentheses themselves

    -- this would be a valid value of inventory_item type defined above
    '("fuzzy dice",42,1.99)'
    
- to set a field to `NULL`, write no characters at all in its position (not even a space)

    -- first value is NULL
    '(,42,1.99)'
    
    -- second value is NULL
    '("fuzzy dice",,1.99)'

- to set an empty string rather than `NULL`, write double quotes
    
    -- first field is empty string, third field is NULL
    '("",42,)'

- these constants are initially treated as strings and then passed to the composite-type input conversion routine. An explicit type specification might be necesseray to tell which type to convert the constant to.


## composite values with `ROW` expressions syntax 

    ROW('fuzzy dice', 42, 1.99)
    ROW('', 42, NULL)

- the `ROW` keyword is optional, as long as there's more than one field in the expression 

    ('fuzzy dice', 42, 1.99)
    ('', 42, NULL)

## accessing composite types 

- syntax in query: `([table.]column).field`

    SELECT (item).name FROM on_hand 
    WHERE (item).price > 9.99;

    SELECT (on_hand.item).name FROM on_hand 
    WHERE (on_hand.item).price > 9.99;

- similarly to select fields from the result of a function that returns a composite value

    SELECT (my_func(...)).foo FROM ...

    SELECT (my_func(...)).* FROM ...
    
## modifying composite types
- inserting 

    INSERT INTO mytable (complex_col) VALUES (ROW(1.2,2.2)); 
    
    -- or `ROW` keyword can be omitted here, as explained earlier
    
    INSERT INTO mytable (complex_col) VALUES ((1.2,2.2)); 

    -- insert into specific subfields

    INSERT INTO mytable (complex_col.foo, complex_col.bar) 
    VALUES ((1.2,2.2)); 
    

- updating

    UPDATE mytable SET complex_col.foo = (complex_col).foo + 1 
    WHERE ...;

- note that when writing to composite type, we don't put parentheses around the column name when on the "write" side of the expression, but we include them when on the "read" side of it.
    
## using composite types in queries: 
https://www.postgresql.org/docs/14/rowtypes.html#ROWTYPES-USAGE
- various special syntax rules associated with composite types in queries provide useful shortcuts. But you should know the logic behind.

- a reference to a table name (or alias) in a query is effectively a reference to the composite value of the table's current row.

- simple names are matched to columns names *before* table names. So given the following table

    CREATE TABLE users (
        id      integer,
        name    text,
        role    text,
        u       text,
    );

    -- this query returns a single composite-value column for the table
    SELECT foo from users foo;
    
                 foo 
    ---------------------------
    (342,"bob","admin","hello")

    -- whereas this query returns a single composite-value for an underlying column
    -- i.e. the column takes precedence
    
    SELECT u from users u;
    
        u
    ---------
    ("hello")
    
- the qualified-column-name syntax `table_name.column_name`, however, can be understood as applying field selection to the composite value of the table's current row. i.e. the table name takes precedence.

    SELECT u.* from users u;

      id  | name  | role    |   u
    ---------------------------------
      342 | "bob" | "admin" | "hello"

    
## More 
https://www.postgresql.org/docs/14/rowtypes.html#ROWTYPES-USAGE
https://www.postgresql.org/docs/14/rowtypes.html#ROWTYPES-IO-SYNTAX
https://www.postgresql.org/docs/14/sql-expressions.html#FIELD-SELECTION
    
     
