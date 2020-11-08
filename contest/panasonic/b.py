a, b = map(int, input().split())
if a % 2 == 1 and b % 2 == 1:
    print(int((a * b) // 2) + 1)
else:
    print(int((a * b) // 2))
