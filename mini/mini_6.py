def flatten(a, depth = -1):
    b = []
    for i in a:
        if not isinstance(i, list):
            b.append(i)
        else:
            if depth != 0:
                for j in flatten(i, depth=depth-1 if depth > 0 else -1):
                    b.append(j)
            else:
                b.append(i)

    return b


assert flatten([1, 2, [3, 4], [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7], "Wrong answer"
assert flatten([]) == [], "Wrong answer"
assert flatten(["2", [3, 7897]]) == ["2", 3, 7897], "Wrong answer"
assert flatten([1, 2, [4, 5], [6, [7]], 8], depth=1) == [1, 2, 4, 5, 6, [7], 8], "Wrong answer"

print("ALL TESTS PASSED :D")
