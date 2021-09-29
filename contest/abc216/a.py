x, y = map(int, input().split("."))

if y <= 2:
    ans = "-"
elif y <= 6:
    ans = ""
else:
    ans = "+"

print(str(x) + ans)
