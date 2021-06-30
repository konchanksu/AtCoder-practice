x, y = map(int, input().split())

if x == y:
    print(x)
else:
    [print(i) for i in range(3) if x != i and y != i]
