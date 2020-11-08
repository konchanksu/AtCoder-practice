n, k = map(int, input().split())

a = 10 ** 9 + 7
ans = 0
small = 0
big = 0
for i in range(0 , k):
    big += n - i
    small += i
    
for i in range(k, n + 1):
    ans += big - small + 1
    big += n - i
    small += i

print((ans + 1) % a)
