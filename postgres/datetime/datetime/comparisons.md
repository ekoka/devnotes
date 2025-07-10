- convert to date

    WHERE 
        birthday >= '1999-03-23'::date

- using intervals for calculation 

    WHERE 
        birthday >= ('1999-03-23'::date + '1 day'::interval)
