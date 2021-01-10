N = int(input())
point = [tuple(map(int, input().split())) for i in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if point[i][0] == point[j][0]:
            continue
            
        a = (point[i][1] - point[j][1]) / (point[i][0] - point[j][0])
        if  -1 - 10**(-6) <= a <= 1 + 10**(-6):
            ans += 1
print(ans)
