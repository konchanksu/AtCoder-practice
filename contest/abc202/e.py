from collections import deque

N = int(input())
P = list(map(int, input().split()))
Q = int(input())
Qs = [list(map(int, input().split())) for _ in range(Q)]
BP = [[] for i in range(N+1)]
for i in range(N-2, -1, -1):
    BP[P[i]-1].append(i+1)

for q in Qs:
    r, l = q
    now = r
    branch = 0
    while r != 1:
        branch += 1
        r = P[r-2]

    if l == branch:
        print(1)
    elif l < branch:
        print(0)
    else:
        ans = 0
        l-=branch
        que = deque()
        que.append([now-1, l])
        while que:
            now, l = que.pop()
            if l == 0:
                ans += 1
                continue
            for i in BP[now]:
                que.append([i, l-1])
        print(ans)




