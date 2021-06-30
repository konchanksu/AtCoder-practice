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

    def size(self, a):
        return -self.parents[self.find(a)]

    def group_num(self):
        return len(list(filter(lambda x: x < 0, self.parents)))

    def all_size(self):
        ans = []
        for i in range(self.n):
            if self.parents[i] < 0:
                ans.append(-self.parents[i])
        return ans

n = int(input())
A = list(map(int, input().split()))

error = []
v = {}
num = 0

for i in range(n//2):
    if A[i] != A[n-i-1]:
        error.append((A[i], A[n-i-1]))
        if A[i] not in v:
            v[A[i]] = num
            num += 1
        if A[n-i-1] not in v:
            v[A[n-i-1]] = num
            num += 1

uf = UnionFind(num)

for i, j in error:
    a, b = v[i], v[j]
    uf.union(a, b)

size = uf.all_size()
print(sum(size) - len(size))
