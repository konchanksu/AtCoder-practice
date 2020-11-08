import heapq

N, Q = map(int, input().split())

enji_class = [[] for i in range(N)] # 園児の所属先
class_power = [[] for i in range(2 * 10 ** 5)] # クラスごとの園児の力
max_power = []

for i in range(N):
    a, b = map(int, input().split())
    enji_class[i] = [b - 1, -a]
    heapq.heappush(class_power[b - 1], -a)

C, D = [], [] # C 園児番号 D 幼稚園移動先
for i in range(Q):
    c, d = map(int, input().split())
    C.append(c - 1), D.append(d - 1)

for i in range(2 * 10 ** 5):
    if class_power[i]:
        heapq.heappush(max_power, -class_power[i][0])

for i in range(Q):
    mv_EC, mv_pw = enji_class[C[i]]

    tmp = class_power[mv_EC][0]
    max_power.remove(-tmp)

    class_power[mv_EC].remove(mv_pw)

    if class_power[mv_EC]:
        heapq.heappush(max_power, -class_power[mv_EC][0])
        
    enji_class[C[i]][0] = D[i]
    new_EC = D[i]

    if class_power[new_EC]:
        tmp = class_power[new_EC][0]
        max_power.remove(-tmp)

    heapq.heappush(class_power[new_EC], mv_pw)
    heapq.heappush(max_power, -class_power[new_EC][0])

    max_power.sort()    

    print(max_power[0])

