X = int(input())
a, tmp = 100, 0

while True:
    tmp += 1
    a += a // 100
    if a >= X:
        print(tmp)
        break
