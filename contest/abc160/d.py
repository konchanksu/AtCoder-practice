n, x, y = map(int, input().split())
if x > y:
    x, y = y, x

xy = y - x

ans = [0 for i in range(n)]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if i == j:
            continue
        if (i <= x and j <= x) or (i >= y and j >= y):
            ans[j - i] += 1
        elif i <= x and y <= j:
            ans[j - i - xy + 1] += 1
        else:
            ans[min(j - i, abs(x - i) + abs(y - j) + 1)] += 1

for i in ans[1:]:
    print(i)
