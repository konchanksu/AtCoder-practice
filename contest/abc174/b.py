N, D = map(int, input().split())
ans = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X ** 2 + Y ** 2<= D ** 2 + 0.0000001:
        ans += 1
print(ans)
