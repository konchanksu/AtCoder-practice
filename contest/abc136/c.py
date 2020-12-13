n = int(input())
h = list(map(int, input().split()))

ans = True
h[0] -= 1
for i in range(1, n):
    if h[i - 1] > h[i]:
        ans = False
        break
    if h[i - 1] < h[i]:
        h[i] -= 1

print('Yes' if ans else 'No')
