import inspect
import tempfile

allfunctions = [item[0] for item in inspect.getmembers(tempfile, inspect.isfunction)]
allfunctions.sort()
for item in allfunctions:
    funcname = 'tempfile.' + item
    print("{0}{1}".format(funcname,inspect.formatargspec(*inspect.getfullargspec(eval(funcname)))))