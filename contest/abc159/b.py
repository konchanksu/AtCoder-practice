s = input()
ans = True
for i in range(len(s) // 2):
    if s[len(s) - 1 - i] != s[i]:
        ans = False
if ans:
    for i in range(len(s) // 4):
        if s[(len(s) - 1) // 2 - i - 1] != s[i]:
            ans = False

    for i in range(len(s) // 2 + 1, len(s) // 4 + len(s) // 2 + 1):
        if s[i] != s[len(s) - 1 - i]:
            ans = False

print('Yes' if ans else 'No')

