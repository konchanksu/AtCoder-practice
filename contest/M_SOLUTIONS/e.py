def toridasi(maxitem, nowitem, maxtimes, nowtimes, nowlist):
    if maxtimes == nowtimes:
        ruikei.append(nowlist)
        return
    for ti in range(nowitem, maxitem):
        toridasi(maxitem, ti + 1, maxtimes, nowtimes + 1, nowlist + [ti])
    return

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
tmp = []
ruikei = []

for i in range(N):
    if A[i][0] and A[i][1]:
        tmp.append(A[i])

A, N = tmp, len(tmp)
tatesen, yokosen = {}, {}
tsen, ysen = set(), set()

for i in range(N):
    tsen.add(A[i][0]), ysen.add(A[i][1])
    if A[i][0] in tatesen.keys():
        tatesen[A[i][0]][1].append(i)
    else:
        tatesen[A[i][0]] = [0, [i]]
        tmp = 0
        for j in range(N):
            tmp += abs((A[i][0] - A[j][0]) * A[j][2])
        tatesen[A[i][0]][0] = tmp

    if A[i][1] in yokosen.keys():
        yokosen[A[i][1]][1].append(i)
    else:
        yokosen[A[i][1]] = [0, [i]]
        tmp = 0
        for j in range(N):
            tmp += abs((A[i][1] - A[j][1]) * A[j][2])
        yokosen[A[i][1]][0] = tmp

tsen, ysen = list(tsen), list(ysen)
for i in range(1, N):
    ruikei = []
    toridasi(len(tsen) + len(ysen), 0, i, 0, [])
    tmpmin = float('inf')

    for rui in ruikei:
        tmp, num = set(), 0
        for j in rui:
            if j < len(tsen):
                num += tatesen[tsen[j]][0]
                for k in tatesen[tsen[j]][1]:
                    tmp.add(k)
            else:
                num += yokosen[ysen[j - len(tsen)]][0]
                for k in yokosen[tsen[j - len(tsen)]][1]:
                    tmp.add(k)

        for t in tmp:
            for j in rui:
                if j < len(tsen):
                    if t not in tatesen[tsen[j]][1]:
                        num -= abs(A[t][0] - tsen[j]) * A[t][2]
                else:
                    if t not in yokosen[ysen[j - len(tsen)]][1]:
                        num -= abs(A[t][0] - ysen[j - len(tsen)]) * A[t][2]
        tmpmin = min(tmpmin, num)
    print(tmpmin)
