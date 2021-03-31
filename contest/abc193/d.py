def count(l):
    a = [0] * 10
    ans = 0
    for i in l:
        a[i] += 1
    for i, item in enumerate(a):
        ans += i * (10 ** item)
    return ans

k = int(input())
s = list(map(int, input()[:-1]))
t = list(map(int, input()[:-1]))
win = 0
all = 0

for i in range(1, 10):
    for j in range(1, 10):
        tmp = 0
        if i == j:
            tmp += (k - len(tuple(filter(lambda x:x==i, s))) - len(tuple(filter(lambda x:x==i, t))))
            tmp *= (k - len(tuple(filter(lambda x:x==j, s))) - len(tuple(filter(lambda x:x==j, t)))) - 1
        else:
            tmp += (k - len(tuple(filter(lambda x:x==i, s))) - len(tuple(filter(lambda x:x==i, t))))
            tmp *= (k - len(tuple(filter(lambda x:x==j, s))) - len(tuple(filter(lambda x:x==j, t))))
        all += tmp
        if count(s + [i]) > count(t + [j]):
            win += tmp

print(win / all)
