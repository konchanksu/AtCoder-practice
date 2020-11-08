H, W, K = map(int, input().split())
lists = [input() for i in range(H)]
black, ans = 0, 0
tate, yoko = [0 for i in range(H)],  [0 for i in range(W)]
listskai = [[0 for j in range(W)]for i in range(H)]

for i in range(W):
    for j in range(H):
        if lists[j][i] == '#':
            black += 1
            tate[j] += 1
            yoko[i] += 1
            listskai[j][i] = 1

def tmp(times, num, max, lista, numa):
    if times == 0:
        return lista + [num]

    for tmpi in range(numa + 1, max):
        if tmpi not in num:
            lista = tmp(times - 1, num + [tmpi], max, lista, tmpi)
    return lista

kurono = black

for looph in range(H):
    for j in tmp(looph, [], H, [], -1):
        for loopw in range(W):
            for i in tmp(loopw, [], W, [], -1):
                kurono = black
                for k in i:
                    kurono -= yoko[k]
                    for d in j:
                        kurono += listskai[d][k]

                for d in j:
                    kurono -= tate[d]

                if kurono == K:
                    ans += 1

print(ans)
