N, K = map(int, input().split())
dicts = {i:False for i in range(N)}
for i in range(K):
    d = int(input())
    for j in map(lambda n:int(n) - 1, input().split()):
        dicts[j] = True
        
ans = 0
for i in range(N):
    if not dicts[i]:
        ans += 1

print(ans)
