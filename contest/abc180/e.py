N = int(input())
XYZ = []
for _ in range(N):
    XYZ.append(list(map(int, input().split())))

cost = [[float('inf') for i in range(N)] for j in range(N)]

# コストをsakuseisuru
for i in range(N):
    for j in range(i, N):
        cost[i][j] = abs(XYZ[i][0] - XYZ[j][0]) + abs(XYZ[i][1] - XYZ[j][1]) + max(0, XYZ[j][2] - XYZ[i][2])
        cost[j][i] = abs(XYZ[i][0] - XYZ[j][0]) + abs(XYZ[i][1] - XYZ[j][1]) + max(0, XYZ[i][2] - XYZ[j][2])

# bitDPを試してみる
dp = [[float('inf') for i in range(N)] for _ in range(1 << N)]
dp[0][0] = 0
for i in range(1, N):
    dp[1 << i][i] = cost[0][i]

for S in range(2, 1 << N, 2):
    # v から u へ
    for v in range(N):
        if not (S >> v) % 2:
            continue
        for u in range(N):
            if u == v or not v or not u or (S >> u) % 2:
                continue
            dp[S + pow(2, u)][u] = min(dp[S][v] + cost[v][u], dp[S + pow(2, u)][u])

ans = float('inf')
for i in range(1, N):
    ans = min(ans, dp[pow(2, N) - 2][i] + cost[i][0])

print(ans)
