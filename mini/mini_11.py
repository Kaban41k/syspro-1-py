def cycle(iterable):
    elements = [element for element in iterable]

    while True:
        for element in elements:
            yield element


def chain(*iterables):
    for iterable in iterables:
        for element in iterable:
            yield element


def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break

    return res


assert take(cycle([1, 2, 3]), 10) == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1], "Wrong answer"
assert list(chain([1, 2, 3], ['a', 'b'], ("hello", "world"))) == [1, 2, 3, 'a', 'b', 'hello', 'world'], "Wrong answer"

print("ALL TESTS PASSED :D")
