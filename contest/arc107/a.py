a, b, c, = map(int, input().split())
MOD = 998244353

alist, blist, clist = (1 + a) * a // 2, (1 + b) * b // 2, (1 + c) * c // 2
print(((alist % MOD) * (blist % MOD) % MOD) * (clist % MOD) % MOD)
