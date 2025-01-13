## Using the `time.time()` function

    t1 = time.time()
    r = func()
    t2 = time.time()
    print("%s" % t2-t1)

- make it a decorator
            
    def time_this(fnc):
        def timed_fnc(*a, **kw):
            t1 = time.time()
            r = fnc(*a, **kw)
            t2 = time.time()
            print(f"{fnc.__name__}: Running in {t2-t1}")
            return r
        return timed_fnc

## using the `cProfile` module

    import cProfile, re

    some_regex_pattern = re'(?=[A-Z]{3}([a-z]{5})(?![0-5f-k]{4})'

    cProfile.run('re.compile(some_regex_pattern)')

## using `timeit`
