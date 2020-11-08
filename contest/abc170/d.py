N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
tmp = [True for i in range(A[-1] + 1)]

for i in range(N - 1):
    if tmp[A[i]]:
        if A[i + 1] != A[i]:
            ans += 1
        for j in range(A[i], A[-1] + 1, A[i]):
            tmp[j] = False
if tmp[A[-1]]:
    ans += 1
print(ans) 
