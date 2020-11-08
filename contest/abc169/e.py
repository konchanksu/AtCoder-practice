N = int(input())
A, B = [], []
for i in range(N):
    tm, p = map(int, input().split())
    A.append(tm), B.append(p)
A.sort(), B.sort()

a = A[N // 2] * 2 if N % 2 == 1 else A[N // 2 - 1] + A[N // 2]
b = B[N // 2] * 2 if N % 2 == 1 else B[N // 2 - 1] + B[N // 2]

print((b - a) // 2 + 1 if N % 2 == 1 else b - a + 1)
