from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tmpA = Counter(A)
tmpB = Counter(B)

ans = True
for v, w in tmpA.items():
    if w + tmpB[v] > N:
        ans = False
        break

if not ans:
    print('No')

else:
    print('Yes')

