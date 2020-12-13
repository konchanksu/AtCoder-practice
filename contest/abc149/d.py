n, k = map(int, input().split())
r, s, p = map(int, input().split())
janken = ' '.join(input()).split()

ans = 0

for i, j in enumerate(janken):
    if i - k >= 0 and janken[i-k] == j:
        janken[i] = "j"
        continue

    if j == 'r':
        ans += p
    elif j == 's':
        ans += r
    else:
        ans += s

print(ans)
