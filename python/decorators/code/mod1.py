#bold = '<b>%s</b>' 
#italic = '<i>%s</i>'

def decorator_factory():
    def decorator(fnc):
        def wrapper():
            return italic % (bold % fnc())
        return wrapper
    return decorator



