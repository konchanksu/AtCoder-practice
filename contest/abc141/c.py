n, k, q = map(int, input().split())
a = [int(input()) for i in range(q)]

b = {i:0 for i in range(1, n+1)}
for i in a:
    b[i] += 1

for i in range(1, n+1):
    print('Yes' if k - q + b[i] > 0 else 'No')
