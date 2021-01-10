def gcd(x, y):
    if x < y: x, y = y, x
    while x % y:
        x, y = y, x % y
    return y

a, b, c, d = map(int, input().split())
ans = 0
num_gcd = gcd(c, d)

tmp_min = c-(a%c) + a if a%c != 0 else a
tmp_max = b - (b%c)
if tmp_min <= tmp_max:
    ans += (tmp_max - tmp_min) // c + 1

tmp_min = d-(a%d) + a if a%d != 0 else a
tmp_max = b - (b%d)
if tmp_min <= tmp_max:
    ans += (tmp_max - tmp_min) // d + 1

t = c * d // num_gcd
tmp_min = t-(a%t) + a if a%t != 0 else a
tmp_max = b - (b%t)
if tmp_min <= tmp_max:
    ans -= (tmp_max - tmp_min) // t+1

print(b-a+1-ans)
