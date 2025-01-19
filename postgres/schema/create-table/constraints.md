ref: https://www.postgresql.org/docs/current/sql-createtable.html

### Creating a table

    CREATE TABLE table_name (
        [ { column_declaration | table constraints }, ... ] 
     );

where `column_declaration` is :

        column_name type [column constraints]
        

### Column constraints

    [ CONSTRAINT constraint_name ]
    
    { 
    NOT NULL |
    NULL |
    CHECK ( expression ) [ NO INHERIT ] |
    DEFAULT default_expr |
    GENERATED ALWAYS AS ( generation_expr ) STORED |
    GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY [ ( sequence_options ) ] |
    UNIQUE index_parameters |
    PRIMARY KEY index_parameters |
    REFERENCES reftable [ ( refcolumn ) ] [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ]
        [ ON DELETE referential_action ] [ ON UPDATE referential_action ] 
    }
        
    [ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]

### Table constraints

    [ CONSTRAINT constraint_name ]
    
    { 
    CHECK ( expression ) [ NO INHERIT ] |
    UNIQUE ( column_name [, ... ] ) index_parameters |
    PRIMARY KEY ( column_name [, ... ] ) index_parameters |
    EXCLUDE [ USING index_method ] ( exclude_element WITH operator [, ... ] ) index_parameters [ WHERE ( predicate ) ] |
    FOREIGN KEY ( column_name [, ... ] ) REFERENCES reftable [ ( refcolumn [, ... ] ) ]
        [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ] [ ON DELETE referential_action ] [ ON UPDATE referential_action ] 
    }
        
    [ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]

#### where `referential_action` can be
`NO ACTION` : 
    - the default action.
    - error indicating that the deletion or update would create a foreign key constraint violation. 
    - If the constraint is deferred, this error will be produced at constraint check time if there still exist any referencing rows.

`RESTRICT` : 
    - same as `NO ACTION` except that the check is not deferrable.
    
`CASCADE` : 
    - for delete: delete any rows referencing the deleted row
    - for update: set the values of the referencing column(s) to the new values of the referenced columns.
`SET NULL` :
    - set the referencing column(s) to null.
`SET DEFAULT` : 
    - Set the referencing column(s) to their default values. 
    - a row in the referenced table must match the default values, if they are not null, else the operation will fail.

If the referenced column(s) are changed frequently, it might be wise to add an index to the referencing column(s) so that referential actions associated with the foreign key constraint can be performed more efficiently.
