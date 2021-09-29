N = int(input())
x, y = map(int, input().split())

takotai = [tuple(map(int, input().split())) for _ in range(N)]

inf = float("inf")
dp = [[inf for _ in range(x+1)] for _ in range(y+1)]
next = [[inf for _ in range(x+1)] for _ in range(y+1)]
dp[0][0] = 0

for t in takotai:
    for i in range(x+1):
        for j in range(y+1):
            tx = i+t[0]
            ty = j+t[1]

            if tx > x:
                tx = x
            if ty > y:
                ty = y

            if dp[j][i] != inf:
                next[j][i] = min(dp[j][i], next[j][i])
                next[ty][tx] = min(next[ty][tx], dp[j][i]+1)
    
    for i in range(x+1):
        for j in range(y+1):
            dp[j][i] = next[j][i]
            next[j][i] = inf

if dp[y][x] == inf:
    print(-1)
else:
    print(dp[y][x])
