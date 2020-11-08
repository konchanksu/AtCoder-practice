N = int(input())
x = []
y = []
for i in range(N):
    a = tuple(map(int, input().split()))
    x.append(a[0] + a[1])
    y.append(a[0] - a[1])

x.sort()
y.sort()

print(max(abs(y[0] - y[-1]), abs(x[-1] - x[0])) if x and y else abs(x[-1] - x[0]) if x else abs(y[0] - y[-1]))


