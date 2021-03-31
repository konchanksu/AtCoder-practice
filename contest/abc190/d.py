n = int(input())
ans = 1
tmp = 1
i = 2

while tmp < n:
    tmp += i
    if tmp % i == n % i:
        ans += 1
    i += 1

print(ans * 2)
