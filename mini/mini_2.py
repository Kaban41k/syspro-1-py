def solve(a, b):
    print(list((a[i], b[i]) for i in range((min(len(a), len(b))))))


solve([1, 2, 3], ["a", "b"])