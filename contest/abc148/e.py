N = int(input())

if N % 2:
    print(0)
else:
    ans = 0
    i = 10
    while N >= i:
        ans += N // i
        i *= 5
    
    print(ans)
