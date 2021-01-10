N, M, T = map(int, input().split())
stays = [list(map(int, input().split())) for _ in range(M)]
now = N
time = 0
goal = True

for stay in stays:
    if now <= stay[0] - time:
        goal = False
        break
    now = min(now + time-stay[0]  +stay[1]-stay[0], N)
    time = stay[1]

if goal and T - time < now:
    print("Yes")
else:
    print("No") 
