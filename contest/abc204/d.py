N = int(input())
T = list(map(int, input().split()))

dp = [[float("inf") for j in range(N+1)] for _ in range(10**5+1)]

dp[0][0] = 0
m = 0
for i, t in enumerate(T):
    for l in range(m+1):
        if dp[l][i] == float("inf"):
            continue
        dp[l+t][i+1] = min(dp[l+t][i+1], dp[l][i])
        if l >= dp[l][i] + t:
            dp[l][i+1] = min(dp[l][i+1], dp[l][i] + t)
        else:
            dp[dp[l][i] + t][i+1] = min(dp[dp[l][i] + t][i+1], l)
    m += t

for i in range(10**5):
    if dp[i][N] != float("inf"):
        print(i)
        break
