K = int(input())
if K % 2 == 0 or K % 5 == 0:
    print(-1)
else:
    tmp, i, p = 0, 1, 0
    while True:
        p = (p * 10 + 7) % K
        if not p:
            print(i)
            break
        i += 1
