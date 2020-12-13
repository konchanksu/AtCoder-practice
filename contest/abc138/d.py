import sys
sys.setrecursionlimit(10 ** 8)

n, q = map(int, input().split())
tree = [[] for i in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

point = [0 for i in range(n)]

for _ in range(q):
    p, x = map(int, input().split())
    point[p-1] += x

seen = [False] * n

def dfs(x, val):
    global point
    global seen 
    global tree

    if seen[x]:
        return

    seen[x] = True
    point[x] += val
    for i in tree[x]:
        dfs(i, point[x])

dfs(0, 0)

print(" ".join(list(map(str, point))))
