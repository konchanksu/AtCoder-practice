def isBig(c):
    if ord("A") <= ord(c) <= ord("Z"):
        return True
    return False

def isSmall(c):
    if ord("a") <= ord(c) <= ord("z"):
        return True
    return False

s = input()
ans = True
for i, c in enumerate(s, start=1):
    if i % 2 == 1:
        if not isSmall(c):
            ans = False
            break
    else:
        if not isBig(c):
            ans = False
            break

print("Yes" if ans else "No")
