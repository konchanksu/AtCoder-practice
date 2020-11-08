N, X, T = map(int, input().split())
print((N // X + 1) * T if N % X else (N // X) * T)
