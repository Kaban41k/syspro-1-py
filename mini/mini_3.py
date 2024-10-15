def solve(s):
    return [list(map(float, x.split())) for x in list(s.split("|"))]


print(solve("1 2 | 3 4"))