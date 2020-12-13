n, k = map(int, input().split())
h = list(map(int, input().split()))

for i, H in enumerate(sorted(h, reverse=True)):
    if k > H:
        print(i)
        break
    if i == n-1:
        print(n)
