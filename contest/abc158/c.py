def aaaa(h):
    if h == int(h):
        return int(h)
    else:
        return int(h) + 1

a, b = map(int, input().split())
s = [a / 0.08, (a + 1) / 0.08]
r = [b / 0.1, (b + 1) / 0.1]

for i in range(aaaa(s[0]), aaaa(s[1])):
    for j in range(aaaa(r[0]), aaaa(r[1])):
        if i == j:
            print(i)
            exit()

print(-1)
