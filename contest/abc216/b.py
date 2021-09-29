N = int(input())
names = []
for _ in range(N):
    names.append(tuple(input().split()))

if len(names) == len(set(names)):
    print("No")
else:
    print("Yes")
