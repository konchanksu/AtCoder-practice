N = int(input())
ans = [0 for i in range(N)]

for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            tmp = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if tmp > N:
                break
            ans[tmp - 1] += 1

[print(i) for i in ans]
