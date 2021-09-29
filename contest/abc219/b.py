s = [input() for _ in range(3)]
t = input()
ans = ""

for i in t:
    i = int(i) - 1
    ans += s[i]

print(ans)
