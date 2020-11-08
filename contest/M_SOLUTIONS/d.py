N  = int(input())
A = list(map(int, input().split()))
kabu, money, tmp = 0, 1000, 0

for i in range(N - 1):
    if not kabu and A[i] < A[i + 1]:
        tmp = A[i]
        money, kabu = money % tmp, money // tmp
    elif kabu and A[i] > A[i + 1]:
        money += kabu * A[i]
        kabu = 0

if kabu:
    money += max(tmp, A[-1]) * kabu

print(money)
