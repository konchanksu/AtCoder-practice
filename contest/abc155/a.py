a, b, c = map(int, input().split())

if not a == b == c and (a == b or b == c or a == c):
    print('Yes')
else:
    print('No')
