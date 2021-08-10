from collections import deque

N, M = map(int, input().split())
MOD = 10**9 + 7
INF = float("inf")

g = [[] for _ in range(N)]
already = [False for _ in range(N)]
num = [0 for _ in range(N)]
num[0] += 1
costs = [INF for _ in range(N)]

queue = deque()

for _ in range(M):
    tmp = list(map(int, input().split()))
    g[tmp[0]-1].append(tmp[1]-1)
    g[tmp[1]-1].append(tmp[0]-1)

queue.append([0, 0])

while queue:
    now, cost = queue.popleft()
    
    if N-1 == now:
        break
    if already[now]:
        continue
    already[now] = True
        
    for i in g[now]:
        if costs[i] > cost:
            costs[i] = cost
            num[i] = num[now]
            num[i] %= MOD
            queue.append([i, cost+1])
        elif costs[i] == cost:
            num[i] += num[now]
            num[i] %= MOD

print(num[N-1])
    