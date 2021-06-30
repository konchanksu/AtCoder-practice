n, q = map(int, input().split())
a = list(map(int, input().split()))
num = [0]
for i, o in enumerate(a, start=1):
    num.append(o-i+1)
num.append(10**18+1)

for _ in range(q):
    k = int(input())
    yes, no = 0, n+1
    while abs(yes-no) >= 2:
        mid = (yes + no) // 2
        if num[mid] <= k:
            yes = mid
        else:
            no = mid
    print(yes+k)
