n = int(input())
h = list(map(int, input().split()))

tmp, ans = 0, 0
for i in range(1, len(h)):
    if h[i] <= h[i - 1]:
        tmp += 1
        ans = max(tmp, ans)
    else:
        tmp = 0

print(ans) 
