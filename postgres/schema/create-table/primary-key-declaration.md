#### declaration on a column
syntax:

    column_name data_type [column constraints declaration] PRIMARY KEY [index_parameter]

in context:

    CREATE TABLE table_name ([
        [ column or table constraints declarations, ... ]
        
        column_name data_type [column constraints declaration] PRIMARY KEY [index_parameter],
        
        [..., column or table constraints declarations ]
    ]);

#### declaration on a table
syntax:

    PRIMARY KEY ( column_name [, ... ]) index_parameter
    
in context:

    CREATE TABLE [IF NOT EXISTS] table_name ([
        [ column or table constraints declarations, ... ]
        
        PRIMARY KEY ( column_name [, ... ]) [index_parameter]
        
        [..., column or table constraints declarations ]
    ]);

#### where `[index_parameter]` are

    [ INCLUDE ( column_name [, ... ] ) ]
    [ WITH ( storage_parameter [= value] [, ... ] ) ]
    [ USING INDEX TABLESPACE tablespace_name ]

see also:
https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS
https://www.postgresql.org/docs/current/sql-createtable.html#id-1.9.3.85.9.15
