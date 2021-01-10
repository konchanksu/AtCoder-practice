N, M = map(int, input().split())
A = M**2
print((pow(10 % A, N, A) - pow(10 % M, N, M)) // M)
