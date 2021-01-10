N, K = map(int, input().split())
A = list(map(int, input().split()))

ruiseki = [0]
for a in A:
    ruiseki.append(ruiseki[-1]+a)

ans = 0
for start in range(N):
    if ruiseki[-1] - ruiseki[start] < K:
        continue
    ok = N
    ng = start
    while abs(ok - ng) > 1:
        mid = (ok+ng) // 2
        if ruiseki[mid] - ruiseki[start] >= K:
            ok = mid
        else:
            ng = mid
    ans += N - ok + 1
print(ans)
