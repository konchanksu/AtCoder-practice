n, a, b = map(int, input().split())

if a == 0:
    print(0)
    exit()

ans = (n // (a + b)) * a
if n % (a + b) >= a:
    ans += a
else:
    ans += n % (a + b)

print(ans)
