class unionfind():
    def __init__(self, n):
        self.parents = [-1 for i in range(n)]

    def find(self, a):
        if self.parents[a] < 0:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if x < y:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self):
        return len(list(filter(lambda x: x < 0, self.parents))) - 1

n, m = map(int, input().split())
uf = unionfind(n)
for i in range(m):
    tmp = list(map(int, input().split()))
    uf.union(tmp[0] - 1, tmp[1] - 1)

print(uf.size())
