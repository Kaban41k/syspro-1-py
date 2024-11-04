from functools import partial


def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=None, will_be_removed=None)

    if since is None:
        print(f"Warning: function {f.__name__} is deprecated.", end="")
    else:
        print(f"Warning: function {f.__name__} is deprecated since version{since}.")

    if will_be_removed is None:
        print(f" It will be removed in future versions.")
    else:
        print(f" It will be removed in version {will_be_removed}")

    def inner(*args, **kwargs):
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
