def f(y):
    global x
    ans = 0
    for i, a in enumerate(x[::-1]):
        ans += int(a) * (y**i)
    return ans

x = input()
m = int(input())
maxN = max(map(int, x))

if len(x) == 1:
    if int(x) <= m:
        print(1)
    else:
        print(0)
else:
    ok, ng = maxN, m+1
    
    while abs(ok - ng) > 1:
        tmp = (ok + ng) // 2
        if f(tmp) > m:
            ng = tmp
        else:
            ok = tmp
    print(ok - maxN)
