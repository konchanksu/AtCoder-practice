H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

yoko_sum = [sum([A[h][w] for h in range(H)]) for w in range(W)]
tate_sum = list(map(sum, A))

for h in range(H):
    for w in range(W):
        print(yoko_sum[w] + tate_sum[h] - A[h][w], end=" ")
    print()
