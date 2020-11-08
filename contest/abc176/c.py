N = int(input())
A = list(map(int, input().split()))

tmpmax, ans = A[0], 0
for i in A[1:]:
    if i > tmpmax:
        tmpmax = i
    elif i < tmpmax:
        ans += tmpmax - i

print(ans)
