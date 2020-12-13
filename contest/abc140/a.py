n = int(input())
t = [str(i) for i in range(1, n+1)]
ans = 0

for i in range(100, 1000):
    tmp = True
    for j in str(i):
        if j not in t:
            tmp = False
            break
    if tmp:
        ans += 1

print(ans)
