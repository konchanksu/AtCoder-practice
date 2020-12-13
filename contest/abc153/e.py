H, N = map(int, input().split())
M = [tuple(map(int, input().split())) for i in range(N)]
Mmax = max(M, key=lambda x: x[0])[0]
dp = [0 for i in range(H + Mmax + 1)]

for i in range(1, H + 1 + Mmax):
    dp[i] = min(dp[max(0, i - a)] + b for a, b in M)

print(min(dp[H:]))
