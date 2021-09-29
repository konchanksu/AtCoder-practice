n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
inf = float("inf")
ans = [inf for _ in range(n)]
now = inf

for i in range(n):
    if now > T[i]:
        now = T[i]
    ans[i] = now
    now += S[i]

for i in range(n):
    if now > T[i]:
        now = T[i]
    ans[i] = now
    now += S[i]

[print(i) for i in ans]

