s = input()
l = set(s)
ans = False if len(l) == 1 else True
tmp = True

for i in range(1, 4):
    if (int(s[i-1])+1) % 10 != int(s[i]):
        tmp = False
        break

if tmp:
    ans = False

print("Weak" if not ans else "Strong")
