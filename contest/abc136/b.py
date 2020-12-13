n = int(input())
length = len(str(n))
ans = 0
for i in range(1, length, 2):
    ans += 9 * 10**(i-1)

if length % 2 == 1:
    ans += n - 10**(length-1) + 1

print(ans)
