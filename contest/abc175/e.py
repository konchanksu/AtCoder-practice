R, C, K = map(int, input().split())
r, c, v = [], [], []
rootmap = [[0 for j in range(C)] for i in range(R)]
dp = [[[0 for _ in range(4)] for j in range(C)] for i in range(R)]

for i in range(K):
    tmp = list(map(int, input().split()))
    rootmap[tmp[0] - 1][tmp[1] - 1] = tmp[2]

for t in range(R + C - 1):
    for j in range(0, C):
        i = t - j
        if i >= R or i < 0:
            continue
        for k in range(3):
            if i > 0:
                dp[i][j][k + 1] = max(dp[i][j][k], dp[i - 1][j][k - 1] + rootmap[i][j])
            if j > 0:
                dp[i][j][k + 1] = max(dp[i][j][k], dp[i][j - 1][k - 1] + rootmap[i][j])

print(dp)
