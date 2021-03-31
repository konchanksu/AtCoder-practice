def turn(x, y, reverse=False):
    if reverse:
        return [-y, x]
    return [y, -x]

def symmetric(x, y, axis=0, is_x=True):
    if is_x:
        return [x-(x-axis)*2, y]
    return [x, y-(y-axis)*2]

N = int(input())
zahyou = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
op = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
qu = [tuple(map(int, input().split())) for _ in range(Q)]

a = [0, 0]
b = [0, 1]
c = [1, 0]

data = [[[0, 0], [0, 1], [1, 0]]]


for i in range(M):
    if op[i][0] == 1:
        a = turn(*a)
        b = turn(*b)
        c = turn(*c)
    elif op[i][0] == 2:
        a = turn(*a, reverse=True)
        b = turn(*b, reverse=True)
        c = turn(*c, reverse=True)
    elif op[i][0] == 3:
        a = symmetric(*a, op[i][1])
        b = symmetric(*b, op[i][1])
        c = symmetric(*c, op[i][1])
    elif op[i][0] == 4:
        a = symmetric(*a, op[i][1], is_x=False)
        b = symmetric(*b, op[i][1], is_x=False)
        c = symmetric(*c, op[i][1], is_x=False)
    data.append([a, b, c])

for i in range(Q):
    now = zahyou[qu[i][1]-1]
    o = data[qu[i][0]][0]
    x = [data[qu[i][0]][2][j] - o[j] for j in range(2)]
    y = [data[qu[i][0]][1][j] - o[j] for j in range(2)]
    if x[0] == 0:
        print(o[0] + y[0] * now[1], o[1] + x[1] * now[0])
    else:
        print(o[0] + x[0] * now[0], o[1] + y[1] * now[1])

