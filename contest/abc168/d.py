from collections import deque
class UnionFind:
    def __init__(self, N):
        self.parents = [-1 for i in range(N)]
        self.unit = [0 for i in range(N)]
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if x > y:
            x, y = y, x
            
        self.parents[x] += self.parents[y]
        self.parents[y] = x

N, M = map(int, input().split())
uf = UnionFind(N)


lists = [False for i in range(N)]
lists[0] = True
a = N - 1
dicts = {i:[] for i in range(N)}
d = deque([0])

for i in range(M):
    tmpa, tmpb = map(lambda x: int(x) - 1, input().split()) 
    dicts[tmpa] += [tmpb]
    dicts[tmpb] += [tmpa]
    uf.union(tmpa, tmpb)

if -uf.parents[0] == N:
    print('Yes')
    while a > 0:
        tmp = d.popleft()
        for i in dicts[tmp]:
            if not lists[i]:
                if tmp != 0:
                    lists[i] = tmp
                else:
                    lists[i] = -1
                d.append(i)
                a -= 1
    
    for i in range(1, N):
        print(lists[i] + 1 if lists[i] != -1 else 1)
else:
    print('No')
