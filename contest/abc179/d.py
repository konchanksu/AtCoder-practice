n, k = map(int, input().split())
l, r = [], []
mod = 998244353

for i in range(k):
    tmp = tuple(map(int, input().split()))
    l.append(tmp[0]), r.append(tmp[1])

dp = [0 for i in range(n)]
dp[0] = 1

for i in range(1, n):
    dp[i] = dp[i - 1]
    for j in range(k):
        if r[j] >= 0:
            dp[i] += dp[i - l[j] + 1] - dp[i - r[j]]
            dp[i] %= mod
        if l[j] == 0:
            dp[i] += 1

print(dp[n - 1] % mod)
