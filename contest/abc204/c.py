from collections import deque

N, M = map(int, input().split())

city = [[] for _ in range(N)]
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    city[a-1].append(b-1)


for i in range(N):
    already = [False for _ in range(N)]
    queue = deque()
    queue.append(i)
    
    while queue:
        now = queue.popleft()
        if already[now]:
            continue
        
        already[now] = True
        ans += 1
        
        for j in city[now]:
            queue.append(j)

print(ans)
