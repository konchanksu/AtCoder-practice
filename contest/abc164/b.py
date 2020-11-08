a, b, c, d = map(int, input().split())
print('Yes' if int(c / b + 0.9999) <= int(a / d + 0.9999) else 'No')
