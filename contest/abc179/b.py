N = int(input())
tmp = 0
ans = False

for i in range(N):
    tmp += 1
    t = tuple(map(int, input().split()))
    if t[0] != t[1]:
        tmp = 0
    if tmp >= 3:
        ans = True

print('Yes' if ans else 'No')
