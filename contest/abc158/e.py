n, p = map(int, input().split())
s = input()
ans = 0
for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        if int(s[j:j + i]) % p == 0:
            ans += 1

print(ans)
