def specialize(f, *a, **k):
    def f_modifire(*args, **kwargs):
        new_f = f(*a, *args, **k, **kwargs)
        return new_f
    return f_modifire


def my_sum(x, y):
    return x + y


plus_one = specialize(my_sum, y=1)
just_two = specialize(my_sum, 1, 1)

assert plus_one(10) == 11, "Wrong answer"
assert just_two() == 2, "Wrong answer"
assert specialize(str, 123)() == "123", "Wrong answer"
assert list(specialize(map, int)(["1", "2"])) == [1, 2], "Wrong answer"

try:
    assert specialize(my_sum, z=12)()
    exit(1)
except:
    pass

print("ALL TESTS PASSED :D")