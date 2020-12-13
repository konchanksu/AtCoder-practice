N = int(input())

point = []

for _ in range(N):
    point.append(list(map(int, input().split())))
   
ans = False
for i in range(len(point)):
    for j in range(i + 1, len(point)):
        for k in range(j + 1, len(point)):
           if (point[i][1] - point[j][1]) * (point[i][0] - point[k][0]) == (point[i][0] - point[j][0]) * (point[i][1] - point[k][1]):
               ans = True
               
if ans:
    print("Yes")               
else:
    print("No")

               