from collections import deque

N = int(input())
K = int(input())
S = [input() for _ in range(N)]
already = [[False for _ in range(N)] for _ in range(N)]

pattern = set()

for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            continue
        stack = deque()
        stack.append(((i, j),))
        while stack:
            crs = stack.pop()
            
            if len(crs) == K:
                pattern.add(tuple(sorted(crs)))
                continue

            for now in crs:
                if already[now[0]][now[1]]:
                    continue
                for c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next = (now[0] + c[0], now[1] + c[1])
                    if next[0] < 0 or next[0] >= N or next[1] < 0 or next[1] >= N:
                        continue
                    if S[next[0]][next[1]] == "#":
                        continue
                    if next in crs:
                        continue
                    stack.append(crs+(next,))
        already[i][j] = True
print(len(pattern))
            