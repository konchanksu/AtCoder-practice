n, x = map(int, input().split())
now = 0
a = False
for i in range(n):
    v, p = map(int, input().split())
    now += v * p / 100
    if now >= x + 0.00000001:
        print(i+1)
        a = True
        break
if not a:
    print(-1)

