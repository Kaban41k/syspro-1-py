from functools import *


def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=since, will_be_removed=will_be_removed)

    @wraps(f)
    def inner(*args, **kwargs):
        print(f"Warning: function {f.__name__} is deprecated", end="")

        if since is not None:
            print(f" since version {since}", end="")

        print(". It will be removed in ", end="")

        if will_be_removed is None:
            print(f"future versions.")
        else:
            print(f"version {will_be_removed}.")

        ret = f(*args, **kwargs)
        return ret

    return inner


@deprecated
def foo():
    print("Hello from foo")


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")


@deprecated(since="1.12.2")
def baz():
    print("Hello from baz")


foo()
bar()
baz()
