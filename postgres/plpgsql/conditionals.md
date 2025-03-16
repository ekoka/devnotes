
ref: https://www.postgresql.org/docs/current/plpgsql-control-structures.html#PLPGSQL-STATEMENTS-CALLING-PROCEDURE

## IF statement

    IF / THEN / END IF
    IF / THEN / ELSE / END IF
    IF / THEN / ELSIF / THEN / ELSE / END IF

-  syntax

    IF boolean-expression THEN
        statements
    ELSIF
        statements
    ELSE
        statements
    END IF 

e.g.

    IF number = 0 THEN
        result := 'zero';
    ELSIF number > 0 THEN
        result := 'positive';
    ELSIF number < 0 THEN
        result := 'negative';
    ELSE
        -- hmm, the only other possibility is that number is null
        result := 'NULL';
    END IF;

    -- or embedded IFs
    IF demo_row.sex = 'm' THEN
        pretty_sex := 'man';
    ELSE
        IF demo_row.sex = 'f' THEN
            pretty_sex := 'woman';
        END IF;
    END IF;

    
        
- note that `ELSIF` can also be spelled `ELSEIF`
        
## CASE statement

    CASE / WHEN / THEN / ELSE / END CASE
    CASE WHEN / THEN / ELSE / END CASE

- e.g. simple CASE

    CASE search-expression
        WHEN expression [, expression [...]] THEN
            statements
        [WHEN expression [, expression [...]] THEN
            statements
        ...]
        [ELSE
            statements]
    END CASE;

- `search-expression` is evaluated once and successively compared to each expression in the `WHEN` clauses.
- if a match is found the corresponding statements are executed, then control is passed to the next statement after `END CASE`. 
- subsequent `WHENS` are not evaluated.
- if no match is found the `ELSE` statements are executed if present, if not, a `CASE_NOT_FOUND` exception is raised.

- searched CASE

    CASE 
        WHEN boolean-expression THEN
            statements
        [ WHEN boolean-expression THEN
            statements
        ...]
        [ELSE
            statements]
    END CASE;


- e.g. 
    CASE
    WHEN x BETWEEN 0 AND 10 THEN
        msg := 'value is between zero and ten';
    WHEN x BETWEEN 11 AND 20 THEN
        msg := 'value is between eleven and twenty';
END CASE;
