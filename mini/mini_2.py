def my_zip(a, b):
    return [(a[i], b[i]) for i in range(min(len(a), len(b)))]


assert my_zip([1, 2, 3], ["a", "b"]) == [(1, 'a'), (2, 'b')], "Wrong answer"
assert my_zip([], []) == [], "Wrong answer"
assert my_zip([], [1, 2]) == [], "Wrong answer"
assert my_zip([1], []) == [], "Wrong answer"
assert my_zip([1, 22], ["dasdf", "dfs"]) == [(1, 'dasdf'), (22, 'dfs')], "Wrong answer"

print("ALL TESTS PASSED :D")
