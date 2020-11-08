X = int(input())

lists = [i ** 5 for i in range(1000)]

for a, i in enumerate(lists):
    for b, j in enumerate(lists):
        if X == i - j:
            print(a, b)
            exit()
        elif X == i + j:
            print(a, -b)
            exit()    
