H, W, M = map(int, input().split())
hallline = [0 for i in range(H)]
wallline = [0 for i in range(W)]
b = {}

for i in range(M):
    tmp = list(map(lambda x: int(x) - 1, input().split()))
    hallline[tmp[0]] += 1
    wallline[tmp[1]] += 1
    b[(tmp[0], tmp[1])] = True

t = max(hallline)
s = max(wallline)

a = [i for i in range(H) if hallline[i] == t]
c = [i for i in range(W) if wallline[i] == s]

tmp = False

for i in a:
    for j in c:
        if (i, j) not in b.keys():
            print(t + s)
            tmp = True
            break
    if tmp:
        break
if not tmp:
    print(t + s - 1)
