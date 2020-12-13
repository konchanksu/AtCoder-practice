N = int(input())
P = [[i, j] for i, j in enumerate(map(lambda x:int(x)-1, input().split()))]
cost = [i[0] - i[1] for i in P]

if sum(cost) == 0 and sum(list(filter(lambda x:0>x, cost))) == -N+1 and len(list(filter(lambda x:x==0, cost))) == 0:
    tmp = [(0, 0)]
    for j, i in enumerate(cost):
        tmp.append((tmp[-1][0]+i, j+1))
    
    tmp = tmp[1:-1]
    tmp.sort()
    for i in tmp:
        print(i[1])
    
else:
    print(-1)
