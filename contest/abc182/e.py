H, W, N, M = map(int, input().split())

raze = [[0 for _ in range(W)] for j in range(H)]
ans = [[False for _ in range(W)] for j in range(H)]

for i in range(N):
    a, b = map(lambda x: int(x) - 1, input().split())
    raze[a][b] = 1

for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    raze[a][b] = -1

for i in range(H):
    now = 0
    for j in range(W):
        if raze[i][j] == 1:
            now = 1
        elif raze[i][j] == -1:
            now = 0
        
        if now == 1:
            ans[i][j] = True

for i in range(H):
    now = 0
    for j in range(W - 1, -1, -1):
        if raze[i][j] == 1:
            now = 1
        elif raze[i][j] == -1:
            now = 0
        
        if now == 1:
            ans[i][j] = True

for j in range(W):
    now = 0
    for i in range(H):
        if raze[i][j] == 1:
            now = 1
        elif raze[i][j] == -1:
            now = 0
        
        if now == 1:
            ans[i][j] = True

for j in range(W):
    now = 0
    for i in range(H - 1, -1, -1):
        if raze[i][j] == 1:
            now = 1
        elif raze[i][j] == -1:
            now = 0
        
        if now == 1:
            ans[i][j] = True

answer = 0
for i in range(H):
    for j in range(W):
        if ans[i][j]:
            answer += 1
print(answer)
