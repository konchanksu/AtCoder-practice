n = int(input())
already = {}
fin = int(n ** 0.5) + 1
ans = n

for i in range(2, fin+1):
    j = 2
    while (tmp := (i ** j)) <= n:
        if not already.get(tmp):
            ans -= 1
            already[tmp] = True
        j += 1

print(ans)
