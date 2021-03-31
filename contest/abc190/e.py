from collections import deque
class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
        self.n = n
        self.rank = [0] * n

    def find(self, a):
        if self.parents[a] < 0:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            self.parents[b] += self.parents[a]
            self.parents[a] = b
        else:
            self.parents[a] += self.parents[b]
            self.parents[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

n, m = map(int, input().split())
to = [[] for i in range(n)]
uf = UnionFind(n)
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    to[a].append(b)
    to[b].append(a)
    uf.union(a, b)

k = int(input())
c = list(map(lambda x: int(x)-1, input().split()))
ans = True
for i in range(1, k):
    if uf.find(c[i]) != uf.find(c[i-1]):
        ans = False
        break

if not ans:
    print(-1)
else:
    ans = 0
    for i in range(1, k):
        now = deque()
        for j in to[c[i-1]]:
            now.append((j, 1))
        while True:
            tmp = now.popleft()
            if tmp[0] == c[i]:
                ans += tmp[1]
                break
            for j in to[tmp[0]]:
                now.append((j, tmp[1]+1))
