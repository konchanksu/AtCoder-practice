N = int(input())
people = [list(map(int, input().split())) for i in range(N)]
a = 0

for peopl in people:
    a += peopl[0]

ans = 0
people.sort(reverse=True, key=lambda x: x[0]*2+x[1])
b = 0

for i in range(N):
    a -= people[i][0]
    b += people[i][0] + people[i][1]
    ans += 1
    if a < b:
        break
print(ans)
