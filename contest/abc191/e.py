import heapq
n, m = map(int, input().split())

d = [[] for j in range(n)]
for _ in range(m):
    r = list(map(int, input().split()))
    r[0] -= 1
    r[1] -= 1
    d[r[0]].append((r[1], r[2]))

for i in range(n):
    q = []
    ab = [True for i in range(n)]
    for j, k in d[i]:
        heapq.heappush(q, (k, j))
    a = -1
    while q:
        c, now = heapq.heappop(q)
        if now == i:
            a = c
            break
        if not ab[now]: continue
        ab[now] = False
        for j, k in d[now]:
            heapq.heappush(q, (k+c, j))
    
    print(a)