n = int(input())
a = list(map(int, input().split()))
ans = True

for i, data in enumerate(sorted(a), start=1):
    if i != data:
        ans = False
        break
print("Yes" if ans else "No")
