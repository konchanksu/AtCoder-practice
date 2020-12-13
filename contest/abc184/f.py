import bisect

n, t = map(int, input().split())
A = list(map(int, input().split()))

L, R = [0], [0]

for a in A[:n//2]:
    l = len(L)
    for x in range(l):
        L.append(a+L[x])

for a in A[n//2:]:
    r = len(R)
    for x in range(r):
        R.append(a+R[x])

L.sort()
R.sort()

ans = 0
for l in L:
    if l > t:
        break

    a = R[bisect.bisect_right(R, t-l)-1] + l
    if a > t:
        break

    ans = max(a, ans)
    
print(ans)
    