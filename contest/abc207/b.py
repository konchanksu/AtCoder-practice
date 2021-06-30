a, b, c, d = map(int, input().split())

if b / c >= d:
    print(-1)
else:
    x = 0
    count = 0
    while True:
        a += b
        x += c
        count += 1
        
        if a / x <= d:
            print(count)
            break
    