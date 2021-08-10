n, m = map(int, input().split())
inf = float("inf")
dp = [[inf if i != j else 0 for i in range(n)] for j in range(n)]

for _ in range(m):
    r = tuple(map(int, input().split()))
    dp[r[0]-1][r[1]-1] = r[2]

ans = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
            if dp[i][j] != inf:
                ans += dp[i][j]

print(ans)
