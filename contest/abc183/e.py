h, w = map(int, input().split())
mod = 10 ** 9 + 7
s = [input() for _ in range(h)]

dp = [[0 for i in range(w)] for j in range(h)]
dp[0][0] = 1
X = [[0 for i in range(w)] for j in range(h)]
Y = [[0 for i in range(w)] for j in range(h)]
Z = [[0 for i in range(w)] for j in range(h)]

for i in range(1, h + w + 1):
    for j in range(h):
        y, x = j, i - j
        if x >= w or x < 0:
            continue
        if s[y][x] == "#":
            continue
        
        if x != 0 and s[y][x] != "#":
            X[y][x] = dp[y][x - 1] + X[y][x - 1]
        if y !=  0 and s[y][x] != "#":
            Y[y][x] = dp[y - 1][x] + Y[y - 1][x]
        if y != 0 and x != 0 and s[y][x] != "#":
            Z[y][x] = dp[y - 1][x - 1] + Z[y - 1][x - 1]
        
        dp[y][x] = X[y][x] + Y[y][x] + Z[y][x]
        dp[y][x] %= mod

print(dp[h-1][w-1] % mod)
