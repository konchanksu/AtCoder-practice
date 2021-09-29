import sys

sys.setrecursionlimit(200100)

def dfs(now):
    global next
    global already
    global ans
    if already[now]:
        return -1
    already[now] = True
    ans.append(now+1)
    for i in sorted(next[now]):
        tmp = dfs(i)
        if tmp == 1:
            return 1
        if tmp == 0:
            ans.append(now+1)
    if now == 0:
        return 1
    return 0

N = int(input())
next = [[] for _ in range(N)]
already = [[] for _ in range(N)]
ans = []
for _ in range(N-1):
    tmp = tuple(map(int, input().split()))
    next[tmp[0]-1].append(tmp[1]-1)
    next[tmp[1]-1].append(tmp[0]-1)
dfs(0)
[print(i, end=" ") for i in ans]
print()
