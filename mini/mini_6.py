def flatten(a, depth = -1):
    b = []
    for i in a:
        if not isinstance(i, list) or depth == 0:
            b.append(i)
        else:
            b.extend(flatten(i, depth=depth-1 if depth > 0 else -1))
    return b


assert flatten([1, 2, [3, 4], [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7], "Wrong answer"
assert flatten([]) == [], "Wrong answer"
assert flatten(["2", [3, 7897]]) == ["2", 3, 7897], "Wrong answer"
assert flatten([1, 2, [4, 5], [6, [7]], 8], depth=1) == [1, 2, 4, 5, 6, [7], 8], "Wrong answer"

print("ALL TESTS PASSED :D")
