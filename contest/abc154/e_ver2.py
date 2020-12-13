n, k = input(), int(input())
lenn = len(n)
dp = [[[i] * (k + 1) for i in range(2)] for j in range(lenn + 1)]
print(dp)
