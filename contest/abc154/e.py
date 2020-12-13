def C(n, r):
    ans = 1
    for v, i in enumerate(range(n, n - r, -1), start=1):
        ans *= i / v
    return int(ans)

ans = 0
n, k = input(), int(input())
if len(n) != k:
    ans += C(len(str(n)) - 1, k) * (9 ** k)

if k == 1:
    ans += int(n[0])

else:
    print(aaa(k - 1, n, len(n)))
    ans += aaa(k - 1, n, len(n))

'''
if k == 2:
    for a, b in enumerate(n, start=1):
        if b != '0':
            ans += ((int(n[0])) - 1) * C(len(n) - 1, 1) * 9
            for v, i in enumerate(n[1:], start=2):
                if i != '0':
                    ans += (len(n) - v) * 9 + int(i)
                    break

if k == 3:
    ans += ((int(n[0])) - 1) * 81 * C(len(n) - 1, 2)
    for v, i in enumerate(n[1:], start=2):
        if i != '0':
            ans += ((int(n[v - 1]) - 1)) * 9 * C(len(n[v:]), 1)
            for s, j in enumerate(n[v:], start=v+1):
                if s != '0':
                    ans += (len(n) - s) * 9 + int(j)
                    break

'''


print(ans)
