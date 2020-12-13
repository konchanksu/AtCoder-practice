from collections import deque

H, W = map(int, input().split())
S = [input() for i in range(H)]

ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            queue = deque()
            queue.append([h, w, 0])
            tmpGone = [[False for w in range(W)] for h in range(H)]
            tmpGone[h][w] = True
            tmpMax = [h, w, 0]
            
            while queue:
                now = queue.popleft()
                if tmpMax[2] < now[2]:
                    tmpMax = now
                
                h, w = now[:-1]
                
                if now[0] > 0 and not tmpGone[h-1][w] and S[h-1][w] == ".":
                    queue.append([h-1, w, now[2]+1])
                    tmpGone[h-1][w] = True
                    
                if now[1] > 0 and not tmpGone[h][w-1] and S[h][w-1] == ".":
                    queue.append([h, w-1, now[2]+1])
                    tmpGone[h][w-1] = True
                    
                if now[0] < H-1 and not tmpGone[h+1][w] and S[h+1][w] == ".":
                    queue.append([h+1, w, now[2]+1])
                    tmpGone[h+1][w] = True
                    
                if now[1] < W-1 and not tmpGone[h][w+1] and S[h][w+1] == ".":
                    queue.append([h, w+1, now[2]+1])
                    tmpGone[h][w+1] = True
                    
            ans = max(tmpMax[2], ans)

print(ans)
