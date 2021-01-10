N = int(input())
A = list(map(int, input().split()))

a = A.index(max(A[:2**(N-1)]))
b = A.index(max(A[2**(N-1):]))

print(a+1 if A[a] < A[b] else b+1)
