def flatten(a):
    b = []
    for i in a:
        if not isinstance(i, list):
            b.append(i)
        else:
            for j in flatten(i):
                b.append(j)

    return b

assert flatten([1, 2, [3, 4], [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7], "Wrong answer"
assert flatten([]) == [], "Wrong answer"
assert flatten(["2", [3, 7897]]) == ["2", 3, 7897], "Wrong answer"

print("ALL TESTS PASSED :D")
