n, k = map(int, input().split())

if k > n:
    tmp = n
else:
    tmp = n % k

if tmp > k / 2:
    tmp = k - tmp

print(tmp)
    
