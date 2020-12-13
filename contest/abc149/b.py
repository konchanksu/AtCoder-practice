a, b, k = map(int, input().split())
aa = 0 if k > a else a - k
bb = b if k <= a else b - k + a
if bb < 0:
    bb = 0
print(aa, bb)
