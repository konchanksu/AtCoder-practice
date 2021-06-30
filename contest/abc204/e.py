import heapq

def time(t, c, d):
    if t < d ** (0.5):
        t = int(d**(0.5))
    now = t + c + d // (t+1)

    return now

N, M = map(int, input().split())
road = [[[] for i in range(N)] for j in range(N)]
can = [[] for i in range(N)]

for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    if a == b:
        continue
    road[a][b].append((c, d))
    road[b][a].append((c, d))
    can[a].append(b)
    can[b].append(a)

already = [False for _ in range(N)]
queue = [(0, 0)]

while queue:
    t, now = heapq.heappop(queue)
    
    if already[now]:
        continue
    already[now] = True
    if now == N-1:
        break

    for i in can[now]:
        for cd in road[now][i]:
            heapq.heappush(queue, (time(t, cd[0], cd[1]), i))

print(-1 if not already[N-1] else t)
