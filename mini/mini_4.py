def solve(d):
    new_d = dict()
    a = list(d.keys())
    b = [d[x] for x in a]

    for i in range(len(a)):
        if b[i] in new_d.keys():
            if not isinstance(new_d[b[i]], tuple):
                new_d[b[i]] = [new_d[b[i]]]
            new_d[b[i]] = tuple(list(new_d[b[i]]) + [a[i]])
        else:
            new_d[b[i]] = a[i]

    return new_d


assert solve({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Kuznecov2": 97832}) == {97832: ('Ivanov', 'Kuznecov', 'Kuznecov2'), 55521: 'Petrov'}, "Wrong answer"
assert solve({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}, "Wrong answer"
assert solve({"Ivanov": 97832, "Petrov": 55521}) == {97832: 'Ivanov', 55521: 'Petrov'}, "Wrong answer"
assert solve({4: 3, 1: 2, 8: 2}) == {3: 4, 2: (1, 8)}, "Wrong answer"
assert solve({4: 3, 1: 2}) == {3: 4, 2: 1}, "Wrong answer"
assert solve({4: 3}) == {3: 4}, "Wrong answer"
assert solve({}) == {}, "Wrong answer"


print("ALL TESTS PASSED :D")
