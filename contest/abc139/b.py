a, b = map(int, input().split())

if b == 1:
    print(0)
else:
    a -= 1
    b -= 1
    print(b // a if b % a == 0 else b // a + 1) 
