N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]
d = {}
ans = 0

for c in coords:
    if c[0] not in d:
        d[c[0]] = {c[1]:True}
    else:
        d[c[0]][c[1]] = True

for k in d.keys():
    for k2 in d.keys():
        t = 0
        if k == k2:
            continue
        for s in d[k].keys():
            if s in d[k2]:
                t += 1
        ans += (t-1) * t // 2
print(ans//2)
    
