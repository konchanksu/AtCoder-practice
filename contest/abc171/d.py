N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B, C = [], []
Count = [0 for i in range(10 ** 5 + 1)]
tmp = sum(A)

for i in range(Q):
    b, c = map(int, input().split())
    B.append(b), C.append(c)

for i in A:
    Count[i] += 1

for i in range(Q):
    tmp -= Count[B[i]] * B[i]
    tmp += Count[B[i]] * C[i]
    Count[C[i]] += Count[B[i]]
    Count[B[i]] = 0
    print(tmp)
