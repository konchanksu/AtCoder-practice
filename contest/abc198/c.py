r, x, y = map(int, input().split())

ans = (x**2 + y**2)

ok = 10**20
ng = -1

while abs(ok-ng) >= 2:
    mid = (ok+ng) // 2
    if (mid*r)**2 < ans:
        ng = mid
    else:
        ok = mid

print(ok if r**2 <= ans else 2)
