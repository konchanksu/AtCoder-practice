N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit()

ans = 1
for i in A:
    ans *= i
    
    if ans > 10 ** 18:
        print(-1)
        exit()

print(ans)
