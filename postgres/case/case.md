### search form
- syntax 

    CASE 
        WHEN condition THEN result
        [WHEN ...]
        [ELSE result]
    END

### simple form
        
    CASE expression
        when value THEN result
        [WHEN ...]
        [ELSE result]
    END

- example in `SELECT` query

    select 
        id,
        name, 
        case
            when price > 60 then 
                'expensive'
            when price between 30 and 60 then
                'average'
            when price between 0 and 30 then
                'cheap'
            else 'N/A'
        end as pricing
    from products;

- `CASE` can be used anywhere an expression is valid (e.g. `SELECT`, `WHERE`, `HAVING`, `GROUP BY`, `ORDER BY`)

    - e.g. with `WHERE`
    
    SELECT ... 
    WHERE 
        CASE 
            WHEN x <> 0 THEN y/x > 1.5 
            ELSE false 
        END;
