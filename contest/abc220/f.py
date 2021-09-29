from collections import deque

N = int(input())
tree = {i:[] for i in range(N)}
parent = {i: -1 for i in range(N)}
status = {i: 0 for i in range(N)}
total = {i: 0 for i in range(N)}
already = [False for _ in range(N)]

for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, input().split())
    tree[u].append(v)
    parent[v] = u

stack = deque()
stack.append(0)

while stack:
    num = stack.pop()
    if not already[num]:
        already[num] = True
        stack.append(num)
        for i in tree[num]:
            stack.append(i)
    else:
        for i in tree[num]:
            status[num] = status[i] + 1
            total[num] += status[i] + total[i] + 1


for i in range(N):
    ans = total[i]
    p = i
    while True:
        p = parent[p]
        if p == -1:
            break
        ans += N - status[p]

    print(ans)
