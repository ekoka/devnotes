https://www.postgresql.org/docs/current/sql-createpolicy.html
## Defining a new row-level security policy 
- a policy grants the permission to select, insert, update, or delete rows that match the relevant policy expression

- `CREATE POLICY` command syntax

    CREATE POLICY name ON table_name
    [ AS  { PERMISSIVE | RESTRICTIVE } ]
    [ FOR { ALL | SELECT | INSERT | UPDATE | DELETE } ]
    [ TO { role_name | PUBLIC | CURRENT_ROLE | CURRENT_USER | SESSION_USER } [, ...] ]
    [ USING (using_expression) ]
    [ WITH CHECK (check_expression) ]

- `USING` expression checks existing rows 
- `CHECK` expression checks new rows that would be inserted via `INSERT` or `UPDATE`

- rows are visible when policy expressions (either `USING` or `CHECk`) return `true` and invisible when they return `false` or `null`.

- for `INSERT` and `UPDATE` operations, `CHECK` expressions are enforced after `BEFORE` triggers, which may thus modify the data to be inserted and affect the result of the security policy check.

    INSERT/UPDATE : 
        - BEFORE trigger 
        - CHECK policy

## Enabling Row-Level Security (RLS) on a table 

    ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;

## `PERMISSIVE` vs `RESTRICTIVE` policies
- `PERMISSIVE` policies are combined with `OR`, meaning that users are granted access to a row if at least one of the combined permissive policies allows them access. They're analogous to:
    
    for i = 0 to sizeof(policies):
        if policies[i]:
            return get_row();

- `RESTRICTIVE` policies are combined with `AND`, such that users are granted access to a row if all restrictive policies allow them access. They're analogous to:

    for i = 0 to sizeof(policies):
        if policies[i] is (false or null):
            return;
    return get_row();
