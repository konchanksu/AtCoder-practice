def solve(double, tatami, tate, startW, startH):
    global h, w, ans
    if double == 0:
        ans += 1
        return
    
    if tate:
        for i in range(startW, w):
            tmp = startH if startW == i else 0
            for j in range(tmp, h-1):
                if not tatami[i][j] or not tatami[i][j+1]:
                    continue
                tatami[i][j] = False
                tatami[i][j+1] = False
                solve(double-1, tatami, True, i, j)
                tatami[i][j] = True
                tatami[i][j+1] = True
    
        startH = 0
        startW = 0
    for j in range(startH, h):
        tmp = startW if startH == j else 0
        for i in range(tmp, w-1):
            if not tatami[i][j] or not tatami[i+1][j]:
                continue
            tatami[i][j] = False
            tatami[i+1][j] = False
            solve(double-1, tatami, False, i, j)
            tatami[i][j] = True
            tatami[i+1][j] = True

h, w, a, b = map(int, input().split())
ans = 0

tatami = [[True for i in range(h)] for j in range(w)]

solve(a, tatami, True, 0, 0)

print(ans)
