from collections import deque

H, W = map(int, input().split())
S = [input() for i in range(H)]
tf = [[True if S[j][i] == '.' else False for i in range(W)] for j in range(H)]

for i in range(H):
    for j in range(W):
        if tf:
            queue = deque(i, j, 0)
            while True:
                
            



