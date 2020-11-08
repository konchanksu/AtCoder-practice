N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(min(K, 50)):
    B = [0 for i in range(N)]
    for j in range(0, N):
        l = max(0, j - A[j])
        r = min(N - 1, j + A[j])
        B[l] += 1
        if r + 1 < N:
            B[r + 1] -= 1

    for j in range(1, N):
        B[j] += B[j - 1]
        
    A = B

[print(i, end=' ') for i in B]
print()
