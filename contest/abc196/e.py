def add(a, X):
    return list(map(lambda x:a+x, X))

def max(a, X):
    if X[-1] <= a:
        return [a]
    ok = len(X) - 1
    ng = -1
    
    while abs(ok + ng) < 2:
        mid = (ok + ng) // 2
        if mid > a:
            ok = mid
        else:
            ng = mid
    if ng == -1:
        return X
    else:
        return [a] + X[ok:]

def min(a, X):
    if X[0] >= a:
        return [a]
    ok = 0
    ng = len(X)
    
    while abs(ok + ng) < 2:
        mid = (ok + ng) // 2
        if mid < a:
            ok = mid
        else:
            ng = mid
    if ng == len(X):
        return X
    else:
        return X[:ok] + [a]

N = int(input())
A = []
K = []
for _ in range(N):
    a, k = map(int, input().split())
    A.append(a)
    K.append(k)

Q = int(input())
x = list(map(int, input().split()))

for i in range(N):
    if K == 


