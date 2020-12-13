n, k = map(int, input().split())
S = input()

tmp = 0
for i in range(n-1):
    if S[i] != S[i+1]:
        tmp += 1

ans = n - 1 - tmp

print(ans + 2*k if n > ans + 2*k else n - 1)
