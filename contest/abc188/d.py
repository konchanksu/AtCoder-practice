N, C = map(int, input().split())
date = []
dicts = {}
cost = []

for i in range(N):
    a = list(map(int, input().split()))
    if (a[0]-1) not in dicts:
        dicts[a[0]-1] = [(i, 1)]
    else:
        dicts[a[0]-1] += [(i, 1)]
    if a[1] not in dicts:
        dicts[a[1]] = [(i, -1)]
    else:
        dicts[a[1]] += [(i, -1)]
    date += [a[0]-1, a[1]]
    cost.append(a[2])

ans = 0
date = sorted(list(set(date)))

tmp = 0
for i in dicts[date[0]]:
    tmp += cost[i[0]] * i[1]

for i, d in enumerate(date[1:]):
    if tmp > C:
        ans += C * (d - date[i])
    else:
        ans += tmp * (d - date[i])
    for i in dicts[d]:
        tmp += cost[i[0]] * i[1]
print(ans)
