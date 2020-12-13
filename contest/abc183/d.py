n, w = map(int, input().split())

ruiseki = [0 for _ in range(2 * 10 ** 5 + 2)]
for i in range(n):
    s, t, p = map(int, input().split())
    ruiseki[s] += p
    ruiseki[t] -= p

ans = True
tmp = 0
for i in ruiseki:
    tmp += i
    if tmp > w:
        ans = False
        break

print('Yes' if ans else 'No')
