N = input()

if len(N) % 2 == 0:
    if int(N[:len(N)//2]) <= int(N[len(N)//2:]):
        ans = N[:len(N)//2]
    else:
        ans = int(N[:len(N)//2]) - 1
else:
    ans = "9" * (len(N) // 2)

if len(N) == 1:
    ans = 0
print(ans)
