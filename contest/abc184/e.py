from collections import deque

h, w = map(int, input().split())
a = [input() for _ in range(h)]

dicti = {}

for i in range(h):
    for k in range(w):
        if a[i][k] == "S":
            start = (i, k)
        if a[i][k] == "G":
            goa = (i, k)
        if ord(a[i][k]) >= ord("a") and ord(a[i][k]) <= ord("z"):
            if a[i][k] not in dicti:
                dicti[a[i][k]] = [(i, k)]
            else:
                dicti[a[i][k]] += [(i, k)]
            
gone = [[False for i in range(w)] for j in range(h)]
gone[start[0]][start[1]] = True

queue = deque()
queue.append([start[0] , start[1], 0])
ans = False

while queue:
    now = queue.popleft()
    
    if now[0] == goa[0] and now[1] == goa[1]:
        ans = now[2]
        break
    
    if ord(a[now[0]][now[1]]) >= ord("a") and ord(a[now[0]][now[1]]) <= ord("z"):
        for i in dicti[a[now[0]][now[1]]]:
            if not gone[i[0]][i[1]]:
                queue.append([i[0], i[1], now[2] + 1])
                gone[i[0]][i[1]] = True
                
    if now[0]>0:
        if not gone[now[0]-1][now[1]] and a[now[0]-1][now[1]] != "#":
            gone[now[0]-1][now[1]] = True
            queue.append([now[0]-1, now[1], now[2]+1])
        
    if now[0]<h-1:
        if not gone[now[0]+1][now[1]] and a[now[0]+1][now[1]] != "#":
            gone[now[0]+1][now[1]] = True
            queue.append([now[0]+1, now[1], now[2]+1])
        
    if now[1]>0:
        if  not gone[now[0]][now[1]-1] and a[now[0]][now[1]-1] != "#":
            gone[now[0]][now[1]-1] = True
            queue.append([now[0], now[1]-1, now[2]+1])
        
    if now[1]<w-1:
        if not gone[now[0]][now[1]+1] and a[now[0]][now[1]+1] != "#":
            gone[now[0]][now[1]+1] = True
            queue.append([now[0], now[1]+1, now[2]+1])
              
    gone[now[0]][now[1]] = True

print(ans if ans else -1)
