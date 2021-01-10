MOD = 10**9 + 7
N, M = map(int, input().split())

a = [int(input()) for _ in range(M)]
dp = [0] * (N+1)
dp[0] = 1

for i in a:
    dp[i] = -1
    
for i in range(1, N+1):
    if dp[i] == -1:
        dp[i] = 0
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[N])
