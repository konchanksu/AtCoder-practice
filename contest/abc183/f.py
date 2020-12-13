class uf:
    def __init__(self, n, c):
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n
        self.classnum = [{i:1} for i in c]
    
    def find(self, a):
        if self.parents[a] < 0:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            for k, v in self.classnum[x].items():
                if k in self.classnum[y]:
                    self.classnum[y][k] += v
                else:
                    self.classnum[y][k] = v

            self.parents[y] += self.parents[x]
            self.parents[x] = y
            
        else:
            for k, v in self.classnum[y].items():
                if k in self.classnum[x]:
                    self.classnum[x][k] += v
                else:
                    self.classnum[x][k] = v
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        
    
    def size(self, a, c):
        a = self.find(a)
        return self.classnum[a][c] if c in self.classnum[a] else 0

n, q = map(int, input().split())
C = list(map(int, input().split()))

unf = uf(n, C)
for i in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        unf.union(a, b)
    else:
        b += 1
        print(unf.size(a, b))
    