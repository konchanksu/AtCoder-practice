n, m = map(int, input().split())
jouken = [tuple(map(int, input().split())) for _ in range(m)]

k = int(input())
people = [tuple(map(int, input().split())) for _ in range(k)]
syurui = [[False for _ in range(n)]]

for i in range(k):
    tmp = []
    for s in syurui:
        tmp.append(s[:people[i][0]-1] + [True] + s[people[i][0]:])
        tmp.append(s[:people[i][1]-1] + [True] + s[people[i][1]:])
    syurui = tmp

ans = 0
for i in syurui:
    tmp = 0
    for j in jouken:
        if i[j[0]-1] and i[j[1]-1]:
            tmp += 1
    ans = max(tmp, ans)

print(ans)
