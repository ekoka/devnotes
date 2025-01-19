#### foreign keys are table-level constraints
syntax:

    [ CONSTRAINT constraint_name ] 
        FOREIGN KEY ( column_name [, ... ])
        REFERENCES ref_table [ ( ref_column [, ...] ) ]
        [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ] 
        [ ON DELETE referential_action ] 
        [ ON UPDATE referential_action ] 
    
in context:

    CREATE TABLE [IF NOT EXISTS] table_name ([
        [ column or table constraints declarations, ... ]
        
        [ CONSTRAINT constraint_name ] FOREIGN KEY ( column_name [, ... ]) 
            REFERENCES ref_table [ ( ref_column [, ...] ) ]
            [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ] 
            [ ON DELETE referential_action ] 
            [ ON UPDATE referential_action ] 
        
        [..., column or table constraints declarations ]
    ]);

e.g.

    CREATE TABLE products (
        id uuid PRIMARY KEY, 
        name varchar,
        category_id uuid,
        CONSTRAINT "fkey on categories table" FOREIGN KEY (category_id) REFERENCES categories
    );

#### Dropping foreign key

see also:
https://www.postgresql.org/docs/current/sql-createtable.html
https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK
https://www.postgresql.org/docs/current/tutorial-fk.html
