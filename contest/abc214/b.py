N = int(input())
A = list(map(int, input().split()))

d = {a:i for i, a in enumerate(A, start=1)}

print(d[sorted(A)[-2]])
