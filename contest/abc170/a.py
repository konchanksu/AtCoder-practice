x = list(map(int, input().split()))

for i in range(1, 6):
    if i not in x:
        print(i)
        break
