def bunkatu(now=1, nows=[], all=[]):
    global N
    for i in range(now, N):
        all = bunkatu(i+1, nows + [i], all)
    
    all.append(nows)
    return all

N = int(input())
A = list(map(int, input().split()))

ans = float("inf")

for aaa in bunkatu():
    tmp = 0
    b = 0
    for j in range(N):
        if j in aaa:
            tmp ^= b
            b = 0
        b |= A[j]
    tmp ^= b
    ans = min(tmp, ans)
print(ans)
