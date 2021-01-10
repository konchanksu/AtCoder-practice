n, m = map(int, input().split())
switch = [[] for i in range(n)]
for i in range(m):
    tmp, *a = tuple(map(int, input().split()))
    for j in a:
        switch[j-1].append(i)
is_on = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    lamp = [0 for _ in range(m)]
    tmp = 0
    while i > 0:
        if i % 2 == 1:
            for j in switch[tmp]:
                lamp[j] += 1
        tmp += 1
        i //= 2
    
    isTrue = True
    for j in range(m):
        if lamp[j] % 2 != is_on[j]:
            isTrue = False
            break

    if isTrue:
        ans += 1
print(ans)
    