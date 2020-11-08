N = input()
ans = 0
for i in N:
    ans += int(i)

print('Yes' if not ans % 3 else 'No')
