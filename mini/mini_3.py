def solve(s):
    return [list(map(float, x.split())) for x in list(s.split("|"))]


assert solve("1 2 | 3 4") == [[1.0, 2.0], [3.0, 4.0]], "Wrong answer"
assert solve("") == [[]], "Wrong answer"
assert solve("1") == [[1.0]], "Wrong answer"
assert solve("1 | 2 2 | 333") == [[1.0], [2.0, 2.0], [333.0]], "Wrong answer"

print("ALL TESTS PASSED :D")
