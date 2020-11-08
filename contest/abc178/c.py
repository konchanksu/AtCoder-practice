n = int(input())
MOD = 10 ** 9 + 7
ans = pow(10, n, MOD)
tmp = pow(8, n, MOD)
tmp2 = pow(9, n, MOD)

print((ans + tmp - (tmp2 * 2) % MOD) % MOD)
