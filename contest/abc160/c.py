k, n = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
ans = 0
for i in range(1, n):
    ans = max(ans, abs(a[i - 1] - a[i]))
        
ans = max(abs(a[0] + k - a[n - 1]), ans)

print(k - ans)        
