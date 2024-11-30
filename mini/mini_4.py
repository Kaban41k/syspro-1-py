def solve(d):
    new_d = dict()
    a = list(d.keys())
    b = list(d.values())

    for i in range(len(a)):
        if b[i] in new_d.keys():
            new_d[b[i]] = new_d[b[i]] + tuple([a[i]])
        else:
            new_d[b[i]] = tuple([a[i]])

    for i in range(len(a)):
        if len(new_d[b[i]]) == 1:
            new_d[b[i]] = new_d[b[i]][0]

    return new_d


assert solve({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Kuznecov2": 97832}) == \
             {97832: ('Ivanov', 'Kuznecov', 'Kuznecov2'), 55521: 'Petrov'}, "Wrong answer"
assert solve({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == \
             {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}, "Wrong answer"
assert solve({"Ivanov": 97832, "Petrov": 55521}) == {97832: 'Ivanov', 55521: 'Petrov'}, "Wrong answer"
assert solve({4: 3, 1: 2, 8: 2}) == {3: 4, 2: (1, 8)}, "Wrong answer"
assert solve({4: 3, 1: 2}) == {3: 4, 2: 1}, "Wrong answer"
assert solve({4: 3}) == {3: 4}, "Wrong answer"
assert solve({}) == {}, "Wrong answer"
assert solve({(4,): (3,)}) == {(3,): (4,)}

print("ALL TESTS PASSED :D")
