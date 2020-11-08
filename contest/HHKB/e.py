H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 10 ** 9 + 7

k = sum(s.count('.') for s in S)
ans = (pow(2, k, MOD) * k) % MOD

tate, yoko = [], []

for i in range(H):
    tmp = 0
    tate.append([])
    for j in range(W):
        if S[i][j] == '#':
            for _ in range(tmp):
                tate[i].append(tmp)
            tate[i].append(0)
            tmp = 0
        else:
            tmp += 1
    for _ in range(tmp):
        tate[i].append(tmp)

for i in range(W):
    tmp = 0
    yoko.append([])
    for j in range(H):
        if S[j][i] == '#':
            for _ in range(tmp):
                yoko[i].append(tmp)
            yoko[i].append(0)
            tmp = 0
        else:
            tmp += 1
    for _ in range(tmp):
        yoko[i].append(tmp)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            ans -= pow(2, k + 1 - tate[i][j] - yoko[j][i], MOD)
            ans %= MOD

print(ans)
