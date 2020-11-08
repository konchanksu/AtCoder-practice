from copy import copy

def listmake(n, lists, tmp=[], ans=[]):
    if n == 0:
        ans.append(tmp)
        return ans
        
    for i in lists:   
        a = copy(lists)
        a.remove(i)
        ans = listmake(n - 1, a, tmp + [i], ans)
    return ans 


N = int(input())
X = [[-1 for i in range(N)] for i in range(N)]

for i in range(N):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        X[i][x - 1] = y

for i in range(N):
    ans = True
    if i == 0:
        for k in range(N):
            for s in range(N):
                if X[k][s] == 0:
                    ans = False
        if ans:
            print(N - i)
            exit()
        
    else:
        for j in listmake(i, [k for k in range(N)]):
            ans = True
            for k in range(N):
                if k not in j:
                    for s in range(N):
                        if s in j:
                            if X[k][s] == 1:
                                ans = False
                        else:
                            if X[k][s] == 0:
                                ans = False
                    if not ans:
                        break
                if not ans:
                    break
            if ans:
                print(N - i)
                exit()
                            
print(0)
                                                
                                                        
            
