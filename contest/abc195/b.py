a, b, w = map(int, input().split())

w *= 1000
ans = 0
ans2 = 0
i = 0
can = True

while True:
    i += 1
    if a*i <= w <= b*i:
        ans2 = i
        break
    elif w <= b*i:
        can = False
        break

i = 0
while can:
    i += 1
    if w < a*i:
        ans = i-1
        break

if can:
    print(ans2, ans)
else:
    print("UNSATISFIABLE")
