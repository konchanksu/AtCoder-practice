N = int(input())
a = list(map(int, input().split()))
now = 1

for i in a:
    if i == now:
        now += 1
print(-1 if now == 1 else N - (now-1))
