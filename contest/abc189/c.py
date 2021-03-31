from collections import deque

N = int(input())
A = list(map(int, input().split()))

ans = 0

queue = deque()
queue.append(A)
while queue:
    tmp = queue.popleft()
    if not tmp:
        continue
    m = min(tmp)
    ans = max(m * len(tmp), ans)
    ind = 0
    for i in range(len(tmp)):
        if m == tmp[i]:
            if ind != i:
                queue.append(tmp[ind:i])
            ind = i + 1
    if len(tmp) != ind:
        queue.append(tmp[ind:])

print(ans)

