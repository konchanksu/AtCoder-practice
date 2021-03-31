def floatToInt(a):
    if "." not in a:
        return int(a) * (10 ** 4)
    else:
        for i, c in enumerate(a[::-1]):
            if c == ".":
                break
        return int(a[:-i-1] + a[-i:]) * (10 ** (4 - i))

x, y, r = map(floatToInt, input().split())

x_min = x - r
x_min += 10000 - x_min % (10000) if x_min % 10000 else 0
x_max = x + r
ans = 0

for i in range(x_min, x_max+1, 10000):
    a = r ** 2 - (x - i) ** 2
    a **= 0.5
    pa, na = y + int(a), y - int(a)
    na += 10000 - na % (10000) if na % 10000 else 0
    pa -= pa % (10000)
    ans += pa - na + 10000
print(ans // 10000)
