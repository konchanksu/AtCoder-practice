n, k, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) + k < m * n:
    print(-1)
    exit()
ans = m * n - sum(a) 
print(ans if ans > 0 else 0)
