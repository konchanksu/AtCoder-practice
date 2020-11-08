N = int(input())
A = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def erat():
    end = 10 ** 6 + 1
    t = [False if i == 0 or i == 1 else True for i in range(end)]
    ret = [0 for i in range(end)]

    for i in range(2, end):
        if t[i]:
            for j in range(i * 2, end, i):
                t[j] = False
                if not ret[j]:
                    ret[j] = i
            ret[i] = i
    return ret

tmp = A[0]
for i in A[1:]:
    tmp = gcd(tmp, i)
isS = True if tmp == 1 else False
isP = True

e = erat()

D = dict(iter([(i, False) for i in range(10 ** 6 + 1)]))
for i in A:
    tmp = set()
    while i != 1:
        tmp.add(e[i])
        i //= e[i]
    for i in tmp:
        if D[i]:
            isP = False
            break
        else:
            D[i] = True
    if not isP:
        break

if isP:
    print('pairwise coprime')
elif isS:
    print('setwise coprime')
else:
    print('not coprime')
