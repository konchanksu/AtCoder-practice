l = int(input())
l -= 12

dp = [[0 for j in range(l+1)] for i in range(12)]

dp[0][l] = 1

for i in range(1, 12):
    for j in range(l+1):
        for k in range(j+1):
            dp[i][j-k] += dp[i-1][j]

print(sum(dp[11]))
