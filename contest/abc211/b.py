s = [input() for _ in range(4)]
tmp = ["HR", "H", "2B", "3B"]
ans = True
for i in s:
    if i not in tmp:
        ans = False
        break
    tmp.remove(i)
print("Yes" if ans else "No")
