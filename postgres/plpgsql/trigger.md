https://www.postgresql.org/docs/current/plpgsql-trigger.html

## basic syntax
- a trigger function can be created with PL/pgSQL with the `CREATE FUNCTION` command
- its returns type is `TRIGGER` for a data change trigger or `EVENT_TRIGGER` for database event triggers.
- the function is declared with no arguments
    
    CREATE FUNCTION my_trigger_function RETURNS TRIGGER as 
    $$
        statements
    $$
    language plpgsql;
    
## special variables
- some special `TG_something` local variables describe the context that triggered the call:
    - `TG_NAME`: name of the trigger that fired. Of type `name`. 
    - `TG_WHEN`: `"BEFORE"`, `"AFTER"`, or `"INSTEAD"`. Of type `text`.
    - `TG_LEVEL`: `"ROW"`, `"STATEMENT"`. Of type `text`.
    - `TG_OP`: `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"TRUNCATE"`. Of type `text`.
    - `TG_RELID`: Object ID of the table that caused the trigger. Of type `oid`.
    - `TG_TABLE_NAME`: Name of the table that caused the trigger. Of type `name`.
    - `TG_TABLE_SCHEMA`: Name of the schema of the table that caused the trigger. Of type `name`.
    - `TG_NARGS`: Number of arguments given to the trigger function in the `CREATE TRIGGER` statement. Of type `integer`.
    - `TG_ARGV[]`: Arguments from the `CREATE TRIGGER` statement. The index starts from `0`. Invalid indexes (less than `0` or greater than `TG_NARGS`) result in `NULL`. Of type `array of text`.
    
- in addition to `TG_` variables there are the special `OLD` and `NEW` variables of type `RECORD`, which hold the previous and current db row values for `INSERT/UPDATE` operations in row-level trigger

## return value
- a trigger function must return either `NULL` or a record/row value having exactly the structure of the table the trigger was fired for.

#### `BEFORE` triggers
- if a row-level trigger returns `NULL`, the trigger manager skips the rest of the operation for the row (i.e. subsequent triggers are not fired, and the `INSERT/UPDATE/DELETE` does not occur for the row).

- if a non-null value is returned then the operation proceeds with that row value.
- for `INSERT/UPDATE` triggers, returning a row value different from the original `NEW` value alters the row that will be ultimately inserted or updated. Thus to ensure the `NEW` row is inserted unaltered by the trigger, it must be returned by the trigger function.
- for `DELETE` triggers the returned row has no effect, but it must be non-null for the trigger operation to proceed.
- the return value of *statement-level* triggers is ignored and might as well be `NULL`. However, the operation may still be aborted by raising an error.

#### `AFTER` triggers
- the return value of *row-level* triggers is ignored and might as well be `NULL`. However, the operation may still be aborted by raising an error.

#### `INSTEAD OF` triggers
- always row-level
- only used on views
- can return `NULL` to signal that they did not perform any updates, and that the rest of the operation for this row 
- a non-null value should be returned to signal that the trigger performed the requested operation. 
- 
