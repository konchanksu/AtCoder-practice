N, M = map(int, input().split())
A = list(map(int, input().split()))
route = {}
for _ in range(M):
    x, y = map(int, input().split())
    if y-1 in route:
        route[y-1] += [x-1]
    else:
        route[y-1] = [x-1]

minitem = [A[i] for i in range(N)]
ans = -float("inf")

for i in range(N):
    if i not in route:
        continue
    for j in route[i]:
        ans = max(A[i] - minitem[j], ans)
        if minitem[j] < minitem[i]:
            minitem[i] = minitem[j]

print(ans)
