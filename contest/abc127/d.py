from heapq import *
n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

change = [list(map(int, input().split())) for _ in range(m)]

change.sort(reverse=True, key=lambda x: x[1])

ans = 0
for i in change:
    for j in range(i[0]):
        if not A:
            break
        if A[-1] > i[1]:
            break
        ans += i[1]
        A.pop()
    if not A:
        break

print(sum(A) + ans)
