N = int(input())
A = [float(input()) for i in range(N)]
e = 0.00000000000002
ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if A[i] * A[j] < int(A[i] * A[j]) + e and A[i] * A[j] > int(A[i] * A[j]) - e:
            ans += 1

print(ans)
