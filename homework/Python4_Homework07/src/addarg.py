from functools import wraps
def addarg(arg):
    "return a decorator that adds arg to the decorated function"
    def addarg_decorator(func):
        "Decorate a function to insert arg in the front of the given args"
        @wraps(func)
        def addarg_wrapper(*args, **kw):
            "inserts arg before the wrapped function's args"
            return func(arg, *args, **kw)
        return addarg_wrapper
    return addarg_decorator