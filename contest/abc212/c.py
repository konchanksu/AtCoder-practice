N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
ans = float("inf")
i, j = 0, 0

while i < N and j < M:
    ans = min(abs(A[i] - B[j]), ans)
    if A[i] < B[j]:
        i += 1
    elif A[i] > B[j]:
        j += 1
    else:
        ans = 0
        break

print(ans)
