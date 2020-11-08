n, k = map(int, input().split())
p = list(map(lambda i: (i + 1) / 2, list(map(int, input().split()))))
suma = sum(p[0:k]) 
max = suma
for i in range(k, n):
    suma += (p[i] - p[i - k])
    if suma > max:
        max = suma

print('{:.8f}'.format(max))
