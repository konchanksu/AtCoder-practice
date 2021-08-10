N, A, X, Y = map(int, input().split())

ans = N*X if A >= N else A*X + (N-A) * Y
print(ans)
