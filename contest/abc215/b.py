N = int(input())

for i in range(64):
    if 2 ** i > N:
        print(i-1)
        break
