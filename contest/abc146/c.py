a, b, x = map(int, input().split())

left, right = 0, 10 ** 9+1
while abs(left - right) > 1:
    mid = (left + right) // 2
    if a * mid + b * len(str(mid)) <= x:
        left = mid
    else:
        right = mid

print(left)
