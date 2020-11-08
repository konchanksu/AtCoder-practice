class Unionfind:
    def __init__(self, n):
        self.parents = [-1 for i in range(n)]
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def notsame(self, x, y):
        x = self.find(x)
        y = self.find(y)
        return False if x == y else True
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        if x > y:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def belong_num(self, x):
        return -self.parents[self.find(x)]
    
N, M, K = map(int, input().split())
lists = [0 for i in range(N)]
uf = Unionfind(N)
for i in range(M + K):
    a, b = map(lambda x:int(x) - 1, input().split())
    if i < M:
        uf.union(a, b)     
    if uf.notsame(a, b) and i >= M:
        continue
    lists[a] += 1
    lists[b] += 1
    
for i in range(N):
    print(uf.belong_num(i) - lists[i] - 1, end=' ')
print()
    