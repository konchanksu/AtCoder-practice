"""
フェニック木 BITの定義
"""
class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    
    def add(self, p, x):
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l, r):
        return self._sum(r) - self._sum(l)

N = int(input())
a = list(map(int, input().split()))

bit = Fenwick_Tree(N)
ans = 0
for i, p in enumerate(a):
    bit.add(p, 1)
    ans += i+1 - bit.sum(0, p+1)

for i in range(N):
    print(ans)
    ans += N-1 - 2*a[i]
