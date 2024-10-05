def solve(x):
    sign = x < 0
    k = sign
    if sign:
        x = -x - 1
    while x != 0:
        k += (x + sign) % 2
        x //= 2
    print(k)


x = int(input())

solve(x)