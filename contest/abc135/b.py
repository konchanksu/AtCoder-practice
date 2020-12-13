N = int(input())
P = list(map(int, input().split()))

tmp = 0
for i, p in enumerate(P, start=1):
    if i != p:
        tmp += 1

print("YES" if tmp <= 2 else "NO")
