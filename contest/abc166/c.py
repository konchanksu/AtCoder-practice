global H, N, M
N, M = map(int, input().split())
H = list(map(int, input().split()))

dicts = {i:True for i in range(N)}
for i in range(M):
    a, b = map(lambda x:int(x) - 1, input().split())
    if H[a] < H[b]:
        dicts[a] = False
    elif H[a] == H[b]:
        dicts[a] = False
        dicts[b] = False
    else:
        dicts[b] = False

ans = 0
for i in range(N):
    if dicts[i]:
        ans += 1

print(ans)
    
