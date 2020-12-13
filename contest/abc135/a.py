a, b = map(int, input().split())

if abs(b-a) % 2 == 0:
    print(min(a, b) + abs(b-a)//2)
else:
    print("IMPOSSIBLE")
