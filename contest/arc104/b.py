from copy import copy
N, S = input().split()
N = int(N)
ans = 0

p = [0, 0, 0, 0]
A = [[0, 0, 0, 0]]

for i in S:
    k = 0 if i == 'A' else 1 if i == 'T' else 2 if i == 'C' else 3
    p[k] += 1
    A.append(copy(p))

for i in range(N + 1):
    tmp = 0 if i % 2 == 0 else 1
    for j in range(tmp, i, 2):
        if A[i][0] - A[j][0] == A[i][1] - A[j][1] and A[i][2] - A[j][2] == A[i][3] - A[j][3]:
            ans += 1

print(ans)
