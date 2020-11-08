n = int(input())
a = list(map(int, input().split()))

dp = [[0 for i in range(n // 2 + 1)] for j in range(n + 1)]

dp[1][1] = a[0]
for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i][(i - 1) // 2] = dp[i - 1][(i - 1) // 2]
        dp[i][(i + 1) // 2] = max(dp[i - 2][(i + 1) // 2 - 1] + a[i - 1], dp[i - 1][(i + 1) // 2])
    else:
        dp[i][(i - 1) // 2] = max(dp[i - 2][(i - 1) // 2 - 1] + a[i - 1], dp[i - 1][(i - 1) // 2])
        if i != n:   
            dp[i][(i + 1) // 2] = dp[i - 2][(i + 1) // 2] + a[i - 1]
        
print(dp[n][n // 2])
