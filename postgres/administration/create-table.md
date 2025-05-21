## defining a new table

##### create an empty table

    -- in a specified schema
    CREATE TABLE myschema.foo();

    -- or in current schema
    CREATE TABLE foo();
    
- temporary tables are in a special (sub)schema associated with the current schema, thus a schema name cannot be given for them. The name of the temporary table must still be different from any other table, sequence, index, view, or foreign table in the schema.

    CREATE TEMPORARY TABLE temp_foo();

## simple `CREATE TABLE` syntax

    CREATE [parameters] TABLE [existence] table_name ([...]);

- where the optional `parameters` can be:
    GLOBAL | LOCAL : 
    { TEMPORARY | TEMP }
    UNLOGGED

- where the optional `existence` is `IF NOT EXIST`

## create partitioned table

    CREATE [parameters] TABLE [existence] table_name partition of parent_table [ defining];


