N = int(input())
W = list(map(int, input().split()))
ans = sum(W)
for i in range(1, N):
    ans = min(abs(sum(W[0:i]) - sum(W[i:])), ans)
print(ans)
