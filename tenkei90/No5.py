N, B, K = map(int, input().split())
C = list(map(int, input().split()))

MOD = 10**9+7
dp = [[0 for i in range(B)] for _ in range(61)]
dp[0][0] = 1

for i in range(1 ,61):
    for j in range(B):
        for k in range(B):
            next = (pow(10, i+1, MOD)*dp[i][j] + dp[i][k]) % B
            dp[i][next] += dp[i][j] * dp[i][k]
            dp[i][next] %= MOD


