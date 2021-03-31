a, b, c = map(int, input().split())

while True:
    if c == 0:
        if a == 0:
            print("Aoki")
            break
        a -= 1
        c += 1
    if c == 1:
        if b == 0:
            print("Takahashi")
            break
        b -= 1
        c -= 1
