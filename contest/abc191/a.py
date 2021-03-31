v, t, s, d = map(int, input().split())
t *= v
s *= v
if t <= d <= s:
    print("No")
else:
    print("Yes")
