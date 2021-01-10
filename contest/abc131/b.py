N, L = map(int, input().split())
aji = [L + i for i in range(N)]
tmp, index = float("inf"), 0
for i, a in enumerate(aji):
    if abs(a) < tmp:
        tmp = abs(a)
        index = i

print(sum(aji) - aji[index])

