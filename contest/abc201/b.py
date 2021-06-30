N = int(input())
Mou = [list(input().split()) for i in range(N)]
Mou = list(map(lambda x: [int(x[1]), x[0]], Mou))

Mou = sorted(Mou)
print(Mou[-2][1])
