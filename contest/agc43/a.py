h, w = map(int, input().split())
s = [] # h, w
for i in range(h):
    s += [','.join(input()).split(',')]

cost = [[10000 for i in range(w)] for j in range(h)]

# h: j,  w: i - j
for hh in range(h):
    for ww in range(w):
        # 初期地点
        if hh == ww == 0:
            cost[0][0] = 0 if s[0][0] == '.' else 1

        if hh < h - 1:
            if s[hh][ww] == '.' and s[hh + 1][ww] == '#':
                cost[hh + 1][ww] = min(cost[hh][ww] + 1, cost[hh + 1][ww])
            else:
                cost[hh + 1][ww] = min(cost[hh][ww], cost[hh + 1][ww])
        if ww < w - 1:
            if s[hh][ww] == '.' and s[hh][ww + 1] == '#':
                cost[hh][ww + 1] = min(cost[hh][ww] + 1, cost[hh][ww + 1])
            else:
                cost[hh][ww + 1] = min(cost[hh][ww], cost[hh][ww + 1])

print(cost[h - 1][w - 1])
