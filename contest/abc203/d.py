n, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
tmp = []
for i in A:
    tmp += i

ans = float("inf")
tmp.sort()
indexes = {j:i for i, j in enumerate(tmp)}
back = {i:j for i, j in enumerate(tmp)}

class BIT():
    def __init__(self, n):
        self.n = n
        self.array = [0 for _ in range(n)]
    
    def add(self, i):
        self._add(i, 1)

    def erase(self, i):
        self._add(i, -1)

    def _add(self, i, x):
        i += 1
        pow2 = i & -i
        while i <= self.n:
            self.array[i-1] += x
            i += pow2
            pow2 *= 2

    def sum(self, i):
        ans = 0
        i += 1
        pow2 = i & -i
        while i > 0:
            ans += self.array[i-1]
            i -= pow2
            pow2 = i & -i
        return ans

def tansaku():
    global bit
    global back
    global n
    global k
    helf = k**2//2
    NG = n**2
    OK = 0
    while abs(NG-OK) > 1:
        mid = (OK+NG)//2
        if bit.sum(mid) > helf:
            NG = mid
        else:
            OK = mid
    return NG

bit = BIT(n**2)

for i in range(k-1, n):
    for j in range(i-k+1, i+1):
        for s in range(i-k+1, i+1):
            bit.add(indexes[A[j][s]])

    ans = min(back[tansaku()], ans)
    
    for j in range(k, n):
        for s in range(i-k+1, i+1):
            bit.erase(indexes[A[j-k][s]])
            bit.add(indexes[A[j][s]])
        ans = min(back[tansaku()], ans)
print(ans)
