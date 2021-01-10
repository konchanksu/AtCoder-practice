n, m = map(int, input().split())

l, r = [], []
for i in range(m):
    tmpa, tmpb = map(int, input().split())
    l.append(tmpa)
    r.append(tmpb)

print(min(r) - max(l) + 1 if min(r) >= max(l) else 0)
