X, Y = map(int, input().split())

print('Yes' if Y % 2 == 0 and X * 2 <= Y and X * 4 >= Y else 'No')
