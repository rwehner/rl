from contextlib import contextmanager

@contextmanager
def novalueerror(raising=True):
    try:
        yield object()
    except ValueError:
        pass
    except Exception as e:
        if raising:
            raise