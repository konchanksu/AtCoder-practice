N = int(input())
P = list(map(int, input().split()))
check = [False for _ in range(200002)]
tmp = 0

for i in P:
    check[i] = True
    if check[tmp]:
        for j in range(tmp, 200002):
            if not check[j]:
                tmp = j
                break
    print(tmp)
