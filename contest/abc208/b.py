p = int(input())

coin = []
tmp = 1
for i in range(1, 11):
    tmp *= i
    coin.append(tmp)

ans = 0
c = 9
while True:
    if p == 0:
        break

    if p < coin[c]:
        c -= 1
        continue
    ans += p // coin[c]
    p = p % coin[c]
    c -= 1

print(ans)
