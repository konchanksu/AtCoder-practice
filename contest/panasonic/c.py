from math import sqrt
a, b, c = map(int, input().split())
print('Yes' if sqrt(a) + sqrt(b) < sqrt(c) else 'No')
