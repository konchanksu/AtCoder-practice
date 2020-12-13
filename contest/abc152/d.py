n = int(input())
ans = 0
a = [[[] for i in range(10)] for j in range(10)]
for i in range(1, n + 1):
    a[int(str(i)[0])][int(str(i)[-1])].append(i)

for i in range(1, 10):
    for j in range(1, 10):
        ans += len(a[i][j]) * len(a[j][i])

print(ans)
