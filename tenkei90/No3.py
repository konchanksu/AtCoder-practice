import heapq

N = int(input())
tree = [[] for i in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

already = [False for _ in range(N)]

ans = (0, 0)
queue = [(0, 0)]
while queue:
    cost, now = heapq.heappop(queue)

    if already[now]:
        continue
    already[now] = True
    
    if ans[0] < cost:
        ans = cost, now

    for i in tree[now]:
        heapq.heappush(queue, (cost+1, i))


cost_ans = 0
already = [False for _ in range(N)]
queue = [(0, ans[1])]
while queue:
    cost, now = heapq.heappop(queue)

    if already[now]:
        continue
    already[now] = True
    
    if cost_ans < cost:
        cost_ans = cost

    for i in tree[now]:
        heapq.heappush(queue, (cost+1, i))

print(cost_ans+1)
