h, wi = map(int, input().split())

s = [input() for i in range(h)]

ans = 0
for i in range(h-1):
    for j in range(wi-1):
        w = 0
        if s[i][j] == ".":
            w += 1
        if s[i][j+1] == ".":
            w += 1
        if s[i+1][j] == ".":
            w += 1
        if s[i+1][j+1] == ".":
            w += 1
        if w == 1 or w == 3:
            ans += 1
        elif w == 2 and (s[i][j] == s[i+1][j+1] or s[i+1][j] == s[i][j+1]):
            ans += 1
            
print(ans)
