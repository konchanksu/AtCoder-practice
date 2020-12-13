n = int(input())

ans = (n // 11) * 2

if n % 11 > 6:
    ans += 2
elif n % 11 != 0:
    ans += 1

print(ans)
