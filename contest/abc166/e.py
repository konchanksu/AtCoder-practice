N = int(input())
A = list((i, j) for i, j in enumerate(map(int, input().split())))
dictL = {}
dictR = {}

ans = 0
for i in range(N):
    l, r = A[i][1] + A[i][0], A[i][0] - A[i][1]
    if l not in dictL:
        dictL[l] = 1
    else:
        dictL[l] += 1
    if r not in dictR:
        dictR[r] = 1
    else:
        dictR[r] += 1

for i in dictL.keys():
    if i in dictR.keys():
        ans += dictL[i] * dictR[i]
        
print(ans)  
