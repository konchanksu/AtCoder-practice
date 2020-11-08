N = int(input())
if N % 10 in [2, 4, 5, 7, 9]:
    ans = 'hon'
elif N % 10 in [0, 1, 6, 8]:
    ans = 'pon'
else:
    ans = 'bon'
print(ans)

