H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
tmp = float("inf")
for i in range(H):
    tmp = min(A[i] + [tmp])

ans = 0
for i in range(H):
    for j in range(W):
        ans += A[i][j] - tmp
print(ans)
