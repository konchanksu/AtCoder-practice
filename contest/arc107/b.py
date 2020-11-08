N, K = map(int, input().split())

K = -K if K < 0 else K
pattern = []
ans = 0

for i in range(K + 2, N * 2 + 1):
    pattern.append(tuple([i, i - K]))
    
for i, j in pattern:
    if i <= N + 1:
        ans += (i - 1) * (j - 1)
    elif j <= N + 1:
        ans += (i - 1 - (i - (N + 1)) * 2) * (j - 1)
    else:
        ans += (i - 1 - (i - (N + 1)) * 2) * (j - 1 - (j - (N + 1)) * 2)
    
print(ans)
