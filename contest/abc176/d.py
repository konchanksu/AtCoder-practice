H, W = map(int, input().split())
C = list(map(lambda x: int(x) - 1, input().split()))
D = list(map(lambda x: int(x) - 1, input().split()))
S = [input() for _ in range(H)]
toGo = [[False if i != C[0] or j != C[1] else True for j in range(W)] for i in range(H)]
queue, mahou = [C], [C]
ans = 0

while True:
    tmp = queue.pop()
    mahou.append(tmp)
    dfs = [tmp]

    while len(dfs):
        a = dfs.pop()
        for move in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            hh, ww = a[0] + move[0], a[1] + move[1]
            if hh >= H or hh < 0 or ww >= W or ww < 0:
                continue

            if not toGo[hh][ww] and S[hh][ww] == '.':
                toGo[hh][ww] = True
                dfs.append([hh, ww])
                mahou.append([hh, ww])

    if toGo[D[0]][D[1]]:
        break

    flag = True
    if not len(queue):
        ans += 1
        for k in mahou:
            for i in range(-2, 3):
                for j in range(-2, 3):
                    h, w = i + k[0], j + k[1]
                    if h >= H or h < 0 or w >= W or w < 0:
                        continue

                    if not toGo[h][w] and S[h][w] == '.':
                        flag = False
                        toGo[h][w] = True
                        queue.append([h, w])
        mahou = []

        if flag:
            print(-1)
            exit()

print(ans)
