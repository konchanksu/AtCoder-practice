X, K, D = map(int, input().split())
if X < 0:
    X = -X

a = X // D
if a > K:
    print(X - K * D)
else:
    if (K - a) % 2:
        print(D - X % D)
    else:
        print(X % D)
    
