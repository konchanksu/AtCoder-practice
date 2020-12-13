import heapq
N, M = map(int, input().split())

salary = [[] for _ in range(10**5+1)]
for _ in range(N):
    a, b = map(int, input().split())
    salary[a].append(-b)

que = []
ans = 0
for i in range(1, M+1):
    for s in salary[i]:
        heapq.heappush(que, s)
    if que:
        ans -= heapq.heappop(que)
print(ans)
