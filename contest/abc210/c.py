from collections import Counter

N, K = map(int, input().split())
C = list(map(int, input().split()))

colors = dict(Counter(C[:K]))
ans = len(colors)
tmp = ans

for i in range(K, N):
    if C[i] not in colors or colors[C[i]] == 0:
        colors[C[i]] = 1
        tmp += 1
    else:
        colors[C[i]] += 1
    colors[C[i-K]] -= 1
    if not colors[C[i-K]]:
        tmp -= 1
    
    ans = max(tmp, ans)

print(ans)
