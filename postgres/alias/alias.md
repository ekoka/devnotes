https://www.postgresql.org/docs/current/queries-table-expressions.html

- alias with columns
    
    FROM table_reference [AS] alias( column1 [, column2 [,...]])

    e.g.

    FROM products
        JOIN (select uid, firstname, lastname from users) AS u(id, first, last)
        ON products.user_id = u.id
