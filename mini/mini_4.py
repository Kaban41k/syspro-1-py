def solve(d):
    new_d = dict()
    a = list(d.keys())
    b = [d[x] for x in a]

    for i in range(len(a)):
        if b[i] in new_d.keys():
            new_d[b[i]] = tuple([new_d[b[i]]]) + tuple([a[i]])
        else:
            new_d[b[i]] = a[i]

    print(new_d)


solve({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832})