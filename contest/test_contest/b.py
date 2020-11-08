n = int(input())
r, b = [], []
for i in range(n):
    x, c = input().split()
    if c == 'R':
        r.append(int(x))
    else:
        b.append(int(x))

r.sort()
b.sort()

for i in r:
    print(i)
for i in b:
    print(i)
