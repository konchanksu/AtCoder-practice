N, K = map(int, input().split())
A = list(map(int, input().split()))
left, right = 0, max(A)
while right - left != 1:
    mid = (left + right) // 2
    tmp = 0
    for i in A:
        tmp += i // mid - 1 if i % mid == 0 else i // mid

    if tmp > K:
        left = mid
    else:
        right = mid

print(right)
