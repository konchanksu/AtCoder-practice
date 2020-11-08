N = int(input())
A, B = [], []
for i in range(N):
    tmpa, tmpb = map(int, input().split())
    A.append(tmpa), B.append(tmpb)

MOD = 10 ** 9 + 7
dictsA = {A[0] / B[0]:1}
dictsB = {-B[0] / A[0]:1}
total = 0
delete = 0

for i in range(1, N):
    total += i
    total %= MOD
    if (A[i] / B[i]) in dictsA.keys():
        dictsA[A[i] / B[i]] += 1
    else:
        dictsA[A[i] / B[i]] = 0
    
    if -(B[i] / A[i]) in dictsB.keys():
        dictsB[-B[i] / A[i]] += 1
    else:
        dictsB[-B[i] / A[i]] = 0
 