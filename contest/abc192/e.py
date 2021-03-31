import heapq

n, m, x, y = map(int, input().split())
x -= 1
y -= 1
station = [[] for _ in range(n)]
gone = [False for _ in range(n)]
gone[x] = True

for _ in range(m):
    a, b, t, k = map(int, input().split())
    station[a-1].append([t, k, b-1])
    station[b-1].append([t, k, a-1])

q = []
for item in station[x]:
    heapq.heappush(q, [item[0], item[2]])

ans = None
while q:
    nowTime, nowP = heapq.heappop(q)
    if nowP == y:
        ans = nowTime
        break
    if gone[nowP]:
        continue
    gone[nowP] = True
    for i, j, k in station[nowP]:
        if nowTime % j == 0:
            heapq.heappush(q, [nowTime + i, k])
        else:
            heapq.heappush(q, [j - nowTime%j + nowTime + i, k])

print(ans if ans is not None else -1)
