a, b, c = map(int, input().split())

if c % 2 == 0:
    a, b = abs(a), abs(b)

if a > b:
    print(">")
elif a == b:
    print("=")
else:
    print("<")

