N = int(input())
tasks = []
for _ in range(N):
    tasks.append(tuple(map(int, input().split())))
tasks.sort(key=lambda x:x[1])
time = 0
ans = True

for task in tasks:
    time += task[0]
    if time > task[1]:
        ans = False
        break
print("Yes" if ans else "No")
