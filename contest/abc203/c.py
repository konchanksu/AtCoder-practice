n, k = map(int, input().split())
friend = []
for i in range(n):
    tmp = list(map(int, input().split()))
    friend.append(tmp)
friend.sort()

toGo = True
now = 0
for p, m in friend:
    if k >= p-now:
        k -= p-now
        now = p
        k += m
    else:
        now += k
        toGo = False
        break

if toGo:
    now += k
print(now)

