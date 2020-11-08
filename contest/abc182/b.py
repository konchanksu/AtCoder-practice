N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(max(A) + 1)]

for i in range(2, max(A) + 1):
    for a in A:
        if a % i == 0:
            ans[i] += 1

s, answ = 0, 0
for i in range(max(A) + 1):
    if s < ans[i]:
        answ = i
        s = ans[i]
print(answ)
