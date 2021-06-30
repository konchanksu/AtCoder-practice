N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

small, big = -float("inf"), float("inf")

for i in range(N):
    small = max(A[i], small)
    big = min(B[i], big)

if small > big:
    print(0)
else:
    print(big - small + 1)
