from collections import deque
N = int(input())

node = [[] for i in range(N)]
tmps = []
for _ in range(N-1):
    tmp = list(map(lambda x: int(x)-1, input().split()))
    tmps.append(tmp[1])
    node[tmp[0]].append(tmp[1])

color = [-1 for i in range(N)]
queue = deque()
queue.append(0)
color[0] = -1

while queue:
    now = queue.popleft()
    
    start = 1
    for i in node[now]:
        if color[now] == start:
            start += 1
        color[i] = start
        start += 1
        queue.append(i)

print(max(color))
[print(color[i]) for i in tmps]
