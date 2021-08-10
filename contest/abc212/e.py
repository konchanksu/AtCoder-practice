# 当然TLE

N, M, K = map(int, input().split())
MOD = 998244353

road = [[] for _ in range(N)]
dp = [[0 for _ in range(N)] for j in range(K+1)]
dp[0][0] = 1

for _ in range(M):
    tmp = list(map(int, input().split()))
    road[tmp[0]-1].append(tmp[1]-1)
    road[tmp[1]-1].append(tmp[0]-1)

for i in range(K):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            dp[i+1][k] += dp[i][j]
            dp[i+1][k] %= MOD

        for k in road[j]:
            dp[i+1][k] -= dp[i][j]
            dp[i+1][k] %= MOD

print(dp[K][0])
