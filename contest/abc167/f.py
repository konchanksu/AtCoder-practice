N = int(input())
S = [input() for i in range(N)]

def brancket(s):
    ans = [0, 0]
    l, r = 0, 0
    for i in s:
        if i == ')':
            if r == 0:
                ans[0] += 1
            else:
                r -= 1
        if i == '(':
            r += 1
    ans[1] = r
    return ans

L, R, tl, tr = 0, 0, False, False
for i in S:
    if (a := brancket(i)) != [0, 0]:
        if a[0] == 0:
            tl = True
        if a[1] == 0:
            tr = True
    L += a[0]
    R += a[1]

if L != 0 or R != 0:
    print('Yes' if tl and tr and L == R else 'No')
else:
    print('Yes')
