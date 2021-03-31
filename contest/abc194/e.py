n, m = map(int, input().split())
a = list(map(int, input().split()))

num = [0 for i in range(n + 2)]
s = 0
for i in range(m):
    num[a[i]] += 1

for i, j in enumerate(num):
    if j == 0:
        s = i
        break

for i in range(m, n):
    num[a[i]] += 1
    num[a[i-m]] -= 1
    if a[i-m] < s and num[a[i-m]] == 0:
        s = a[i-m]

print(s)
