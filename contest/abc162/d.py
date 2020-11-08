n = int(input())
s = input()

dicts = {'R':0, 'G':0, 'B':0}
for i in s:
    dicts[i] += 1

ans = dicts['R'] * dicts['G'] * dicts['B']

for i in range(1, (n - 3) // 2 + 2):
    for j in range(0, n):
        if j + i * 2 >= n:
            break
        if s[j] != s[j + i] and s[j] != s[j + 2 * i] and s[j + i] != s[j + 2 * i]:
            ans -= 1

print(ans)
