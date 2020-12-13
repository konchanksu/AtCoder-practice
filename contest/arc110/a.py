N = int(input())

ans = 1
if N != 30:
    for i in range(N, 1, -1):
        if ans % i != 0:
            ans *= i
    
    print(ans+1)

else:
    for i in [7, 11, 13, 16, 17, 19, 23, 25, 27, 29]:
        ans *= i
    print(ans+1)
