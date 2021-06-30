from copy import copy

N = int(input())
ans = float("inf")
status = [list(map(int, input().split())) for _ in range(N)]

dp = [[copy(status[i]) for i in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        for k in range(5):
            dp[i][j][k] = max(status[i][k], dp[i][j][k])

for i in range(N):
    for j in range(N):
