class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
        self.n = N

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if x > y:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def maxGroup(self):
        return -min(self.parents)

N, M = map(int, input().split())
uf = UnionFind(N)

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    uf.union(a, b)

print(uf.maxGroup())

