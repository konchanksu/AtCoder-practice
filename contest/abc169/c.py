A, B = input().split()
a = B.split('.')
a = a[0] + a[1]
A, B = int(A), int(a)
print((A * B) // 100)
