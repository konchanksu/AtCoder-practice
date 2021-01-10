class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
        self.rank = [0] * n

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

        if self.rank[x] < self.rank[y]:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
        else:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def parent(self):
        tmp = []
        for i, p in enumerate(self.parents):
            if p < 0:
                tmp.append((i, -p))
        return tmp

N, M = map(int, input().split())
uf = UnionFind(N)
hen = {i:[] for i in range(N)}
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    uf.union(a, b)
    hen[a].append(b)
    hen[b].append(a)

