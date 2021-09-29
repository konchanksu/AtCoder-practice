H, W, N = map(int, input().split())
point = [tuple(map(int, input().split())) for _ in range(N)]

a = {j:i for i, j in enumerate(sorted(set(map(lambda x:x[0], point))), start=1)}
b = {j:i for i, j in enumerate(sorted(set(map(lambda x:x[1], point))), start=1)}

for i in point:
    print(a[i[0]], b[i[1]])
