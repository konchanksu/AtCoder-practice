N = int(input())
A = list(map(int, input().split()))

A.sort()
ruiseki = [0]

for i in A:
    ruiseki.append(ruiseki[-1] + i)

ans = 0
for i in range(N):
    ans += A[i]*i - ruiseki[i]

print(ans)
