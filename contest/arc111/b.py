class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
        self.tmp = [0] * n
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
            self.tmp[a] += 1
            return
        if self.rank[a] < self.rank[b]:
            self.parents[b] += self.parents[a]
            self.tmp[b] += self.tmp[a] + 1
            self.parents[a] = b
        else:
            self.parents[a] += self.parents[b]
            self.tmp[a] += self.tmp[b] + 1
            self.parents[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

    def all_size(self):
        return sum(tuple(map(lambda x:min(-x[0], x[1]), filter(lambda x: x[0] < -1, zip(self.parents, self.tmp)))))
    
    def t(self):
        return -sum(list(filter(lambda x: x < -1, self.parents)))

    def group_num(self):
        return len(list(filter(lambda x: x < -1, self.parents)))

N = int(input())
pair = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
kind = len(set(j for i in range(N) for j in pair[i]))
uf = UnionFind(4*10**5)

for i in range(N):
    uf.union(pair[i][0], pair[i][1])

b_kind = len([i for i in range(N) if pair[i][0] != pair[i][1] and uf.parents[pair[i][1]] != -1])

print(kind - uf.t() + min(b_kind, uf.all_size()))
