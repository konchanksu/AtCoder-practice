N, K = map(int, input().split())
A = list(map(lambda x:int(x) - 1, input().split()))

already = [False for i in range(N)]
already[0] = True
tel = [0]

while True:
    tmp = A[tel[-1]]
    tel.append(tmp)
    
    if already[tmp]:
        tel.pop()
        break
        
    already[tmp] = True

for i in range(len(tel)):
    if tel[i] == tmp:
        s = i
        break
        
if K - s >= 0:
    ans = (K - s) % (len(tel) - s) 
    print(tel[ans + s] + 1)
else:
    print(tel[K] + 1)
