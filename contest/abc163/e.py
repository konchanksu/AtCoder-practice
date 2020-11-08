n = int(input())
a = list(map(int, input().split()))

ans = 0
right, left = len(a) - 1, 0
big = 0
num = 0

for i in range(len(a)):
    r, l = False, False
    big, num = 0, 0
    for j in range(len(a)):
        if a[j] * max(abs(right - j), abs(j - left)) >= a[num] * max(abs(right - num), abs(num - left)):
            big = a[j] * max(abs(right - j), abs(j - left))
            num = j
            if abs(right - j) > abs(j - left):
                r = True
                l = False
            else:
                r = False
                l = True       
    
    ans += big
    a[num] = -1
    
    if r:
        right -= 1
    if l:
        left += 1
        
print(ans)        
