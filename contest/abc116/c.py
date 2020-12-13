N = int(input())
A = list(map(int, input().split()))
flower = [0 for i in range(N)]
ans = 0

while True:
    tmp, fin = 0, True
    for i in range(N):
        if A[i] == flower[i]:
            if tmp == i:
                tmp = i+1
                continue
            ans += 1
            for j in range(tmp, i):
                flower[j] += 1
            tmp = i+1
            continue
        
        fin = False
    
    if fin:
        break
    
    if tmp != N:
        for i in range(tmp, N):
            flower[i] += 1
        ans += 1

print(ans)
