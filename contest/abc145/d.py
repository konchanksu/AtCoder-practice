def C(n, r, MOD):
    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= MOD
    fn = f
    inv = pow(f, MOD - 2, MOD)
    
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return fn * invs[r] * invs[n-r] % MOD
    
x, y = map(int, input().split())
MOD = 10 ** 9 + 7

if (x + y) % 3 or min(x, y) * 2 < max(x, y):
    print(0)
else:
    n = (x + y) // 3
    r = (min(x, y) - abs(x - y)) // 3
    
    print(C(n, r, MOD))
