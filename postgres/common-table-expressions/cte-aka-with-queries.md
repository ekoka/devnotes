ref: https://www.postgresql.org/docs/9.1/queries-with.html

# `WITH` queries (Common Table Expression)

- auxiliary statements known as *Common Table Expression* or CTEs meant to be used in a larger query.
- think of CTEs as temporary tables that exist in the span of one query.
- each auxiliary statement in a `WITH` statement can be a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` 
- the `WITH` clause itself is attached to a primary statement that can also be a `SELECT`, `INSERT`, `UPDATE`, or `DELETE`

## `SELECT` in `WITH`

- mainly used to break down complicated queries into simpler parts.

- e.g. the following could be written with nested `SELECT` statements, but the use of `WITH` makes it easier to follow what's going on.

    WITH 
        regional_sales AS (
            SELECT 
                region,
                sum(amount) AS total_sales
            FROM orders
            GROUP BY region
        ), 
        top_regions AS (
            SELECT region
            FROM regional_sales
            WHERE total_sales > (SELECT sum(total_sales)>10 FROM regional_sales)
        )
        SELECT 
            region,
            product,
            sum(quantity) AS product_units,
            sum(amount) AS product_sales
        FROM orders
        WHERE region IN (SELECT region from top_regions)
        GROUP BY region, product;


## recursive queries
- adding the optional `RECURSIVE` modifier changes `WITH` to allow a query to refer to its own output.

- e.g. sum of integers from 1 to 100

    WITH RECURSIVE t(n) AS (
        VALUES (1)
        UNION ALL 
            SELECT n + 1 FROM t WHERE n < 100
    )
    SELECT sum(n) FROM t;

