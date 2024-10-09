def solve(x):
    sign = x < 0
    k = sign
    if sign:
        x = -x - 1
    while x != 0:
        k += (x + sign) % 2
        x //= 2

    return k


tests = {10: 2,
         -123: 3,
         -7: 2,
         1024: 1,
         123456789: 16,
         -1000: 3}

for i in tests.keys():
    print(f"Test {i}: ", end="")
    if solve(i) == tests[i]:
        print("PASSED")
    else:
        print("!!!FAIL!!!")
        break
else:
    print("\nALL TESTS PASSED :D")
