import heapq

N, M = map(int, input().split())
next = [[] for _ in range(N)]
costs = {}
already = [False for _ in range(N)]
ttttt = 0
ans = 0
f = 0

for _ in range(M):
    tmp = list(map(int, input().split()))
    next[tmp[0]-1].append(tmp[1]-1)
    next[tmp[1]-1].append(tmp[0]-1)
    if (tmp[0]-1, tmp[1]-1) not in costs:
        costs[(tmp[0]-1, tmp[1]-1)] = tmp[2]
        costs[(tmp[1]-1, tmp[0]-1)] = tmp[2]
    else:
        if costs[(tmp[0]-1, tmp[1]-1)] > tmp[2]:
            costs[(tmp[0]-1, tmp[1]-1)] = tmp[2]
            costs[(tmp[1]-1, tmp[0]-1)] = tmp[2]
    ttttt += tmp[2]
    if tmp[2] < 0:
        f += tmp[2]

queue = []
heapq.heappush(queue, (0, 0))
while queue:
    cost, p = heapq.heappop(queue)
    if already[p]:
        continue
    already[p] = True
    ans += cost
    if cost < 0:
        f -= cost
    
    for i in next[p]:
        heapq.heappush(queue, (costs[(i, p)], i))

print(ttttt - ans - f)
