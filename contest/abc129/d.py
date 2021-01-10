H, W = map(int, input().split())
S = [input() for _ in range(H)]
akari = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
    tmp = 0
    akari_w = [0] * W
    for w in range(W):
        if S[h][w] == "#":
            if tmp == 0:
                continue
            akari_w[w-1] = tmp
            tmp = 0
        else:
            tmp += 1
    if tmp != 0:
        akari_w[w] = tmp
    
    if S[h][w] != "#":
        akari[h][w] = akari_w[w]
    for w in range(W-2, -1, -1):
        if S[h][w+1] != "#":
            akari_w[w] = akari_w[w+1]
        if S[h][w] != "#":
            akari[h][w] = akari_w[w]

for w in range(W):
    tmp = 0
    akari_h = [0] * H
    for h in range(H):
        if S[h][w] == "#":
            if tmp == 0:
                continue
            akari_h[h-1] = tmp
            tmp = 0
        else:
            tmp += 1
    if tmp != 0:
        akari_h[h] = tmp
    
    if S[h][w] != "#":
        akari[h][w] += akari_h[h]
    for h in range(H-2, -1, -1):
        if S[h+1][w] != "#":
            akari_h[h] = akari_h[h+1]
        if S[h][w] != "#":
            akari[h][w] += akari_h[h]
ans = 0
for h in range(H):
    ans = max(*akari[h], ans)

print(ans-1)
