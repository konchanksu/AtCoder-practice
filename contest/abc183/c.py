n, k = map(int, input().split())

T = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def route(n, li, now):
    if len(now) == n:
        li.append(now)
        return li

    for i in range(n):
        if i not in now:
            li = route(n, li, now + [i])
    
    return li


for i in route(n, [], [0]):
    tmp = 0
    
    for j in range(n - 1):
        tmp += T[i[j + 1]][i[j]]
    tmp += T[i[0]][i[-1]]
    
    if tmp == k:
        ans += 1

print(ans)
