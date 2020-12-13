from copy import copy
n = int(input())
x, y = [], []
for i in range(n):
    q, p = map(int, input().split())
    x.append(q)
    y.append(p)

x1 = copy(x)
y1 = copy(y)

ans = 0
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        ans += ((x1[i] - x[j]) ** 2 + (y1[i] - y[j]) ** 2) ** (1 / 2)
        
      

print(ans * 2 / n)
