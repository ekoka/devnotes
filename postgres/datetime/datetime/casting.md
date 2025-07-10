- postgres specific syntax

    date        :   '1999-02-12'::date
    interval    :   '3 days'::interval

- standard syntax

    date        :   CAST('1999-02-12' AS DATE)
    interval    :   CAST('3 days' AS INTERVAL)
