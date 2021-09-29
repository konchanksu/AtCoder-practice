from collections import deque

N, M = map(int, input().split())
que = deque()
tutu = []
d = {}

for i in range(M):
    tmp = int(input())
    tutu.append(deque(list(map(int, input().split()))))
    num = tutu[-1].pop()
    if num-1 in d:
        que.append(i)
        que.append(d[num-1])
    else:
        d[num-1] = i

while que:
    t = que.pop()
    if not tutu[t]:
        continue
    num = tutu[t].pop()

    if num-1 in d:
        que.append(t)
        que.append(d[num-1])
        continue
    d[num-1] = t

if len(tuple(filter(lambda x: x, tutu))):
    print("No")
else:
    print("Yes")
