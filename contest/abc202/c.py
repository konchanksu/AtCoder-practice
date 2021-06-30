from collections import Counter

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_count = Counter(A)

V = [B[i-1] for i in C]
V_count = Counter(V)
ans = 0

for i in A_count.keys():
    ans += A_count[i] * V_count[i]
print(ans)

