N = int(input())
c = input()
r, ans = 0, 0
for i in c:
    if i == 'R':
        r += 1

for i in range(r, N):
    if c[i] == 'R':
        ans += 1

print(ans)
