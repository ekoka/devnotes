## How `WITH RECURSIVE` work

#### parts of a recursive `WITH` query

- the general form is as follows:

    -- (a)
    WITH RECURSIVE query_name(params) AS (
    
        -- (b)
        non-recursive term

        -- (c)
        UNION | UNION ALL

        -- (d)
        recursive term, which can refer back to (a) by its name (e.g. "query_name")
    )

    -- (e)
    primary outer query;

An auxiliary recursive query `(a)` always starts with a *non-recursive* term `(b)`, followed by an `UNION` or `UNION ALL` clause `(c)`, then a *recursive* term `(d)`, refers back to `(a)` as its input source.

Typically the primary outer query `(e)` is the least important part to understanding the mechanism of a recursive `WITH`. It's enough to understand that it's oblivious to the inner workings of the auxiliary query `(a)` and can simply refer to it by name to pull its results.


#### The simple outline of a recursive query (how does it get evaluated?)
- Let's define `OR` as the outer resultset of `(a)`. That's the resultset the primary query `(d)` can pull data from.
- Let's define `WT` as the working table of `(a)`, the inner data set resulting from running a single iteration within `(a)`. That is the result of either the run of `(b)`, or one cycle of `(d)`.
- Let's define `Temp` as the intermediate table holding the results from a single run of `(d)`.

- The evaluation goes as follows:

1. Evaluate `(b)` once.
    - if `(c)` is an `UNION` (but not `UNION ALL`) discard duplicate rows.
    - add the remaining rows to `WT` and `OR`.

2. For as long as `WT` is not empty, repeat the recursive step of the query: 
    - evaluate `(d)`. Where it refers to `(a)`, the contents of that self-reference is what's currently held in `WT`.
    - if `(c)` is an `UNION` (but not `UNION ALL`), discard all duplicate rows from the results of `(d)`, as well as rows that would create duplicates of rows already present in `OR`.
    - add remaining rows to `OR` and to `Temp`.
    - replace contents of `WT` with `Temp` and empty `Temp`.
    
## Terminal condition
- the recursive part of the recursive query will repeat as long as the working table has records

- recursive queries must ensure to have a base condition that resolve to an empty resultset. 
