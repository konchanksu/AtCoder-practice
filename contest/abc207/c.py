n = int(input())

state = []
for _ in range(n):
    t, l, r = map(int, input().split())
    l *= 2
    r *= 2
    if t in (1, 2):
        
        state.append((l, 1))
    else:
        state.append((l+1, 1))
    if t in (1, 3):
        state.append((r, 2))
    else:
        state.append((r-1, 2))

state.sort(key=lambda x:x[1])
state.sort()

ans = 0
count = 0

for i in state:
    if i[1] == 2:
        count -= 1
    else:
        ans += count
        count += 1

print(ans)
