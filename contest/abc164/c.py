N = int(input())
S = [input() for i in range(N)]

dicts = {}
ans = 0
for i in S:
    if i not in dicts.keys():
        ans += 1
        dicts[i] = 0

print(ans)
