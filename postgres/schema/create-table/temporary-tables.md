- temporary tables are in a special (sub)schema associated with the current schema, thus a schema name cannot be given for them. The name of the temporary table must still be different from any other table, sequence, index, view, or foreign table in the schema.

    CREATE TEMPORARY TABLE temp_foo();

