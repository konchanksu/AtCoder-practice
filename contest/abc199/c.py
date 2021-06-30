N = int(input())
S = list(input())
Q = int(input())

re = False

for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    
    if t == 2:
        re = not re
        continue
    
    if re:
        a = a+N if a < N else a-N
        b = b+N if b < N else b-N
    S[a], S[b] = S[b], S[a]

if not re:
    for i in S:
        print(i, end="")

else:
    for i in S[N:] + S[:N]:
        print(i, end="")
print()
