n, m, q = map(int, input().split())
nimotu = [list(map(int, input().split())) for _ in range(n)]
x = list(map(int, input().split()))

query = [list(map(int, input().split())) for _ in range(q)]

for q in query:
    already = [False for _ in range(n)]
    tmp = sorted(x[0:q[0]-1] + x[q[1]:])
    ans = 0
    for i in tmp:
        now = -1
        for j, item in enumerate(nimotu):
            if already[j]:
                continue
            if item[0] <= i:
                if now != -1:
                    if nimotu[now][1] < item[1]:
                        now = j
                else:
                    now = j
        if now != -1:
            ans += nimotu[now][1]
            already[now] = True
    print(ans)
