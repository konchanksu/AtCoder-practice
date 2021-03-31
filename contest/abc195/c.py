n = int(input())

ans = 0
tmp = 999
i = 0

can = True
if 10**3 > n:
    can = False

while can:
    i += 3
    tmp = 10**i - 1
    if 10**i <= n < 10**(i+3):
        ans += (i//3) * (n-tmp)
        break
    else:
        ans += (i//3) * (10**(i+3) - tmp - 1)

print(ans)
