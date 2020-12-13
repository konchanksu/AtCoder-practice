n = int(input())
a = list(map(int, input().split()))
ball = [None for i in range(n)]

for i in range(n, 0, -1):
    t = 0
    for j in range(i*2, n+1, i):
        t += ball[j-1]
    t %= 2

    if a[i-1] == t:
        ball[i-1] = 0
    else:
        ball[i-1] = 1

tmp = len(list(filter(lambda x: x, ball)))
print(tmp)
if tmp:
    for i in range(n):
        if ball[i]:
            print(i+1, end=" ")
    print()
