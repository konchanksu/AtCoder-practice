global N, M, X
N, M, X = map(int, input().split())
global C, A
C, A = [], []
for i in range(N):
    tmp, *_ = map(int, input().split())
    C.append(tmp), A.append(list(_))
    
def adde(a, b):
    t = []
    for i in range(M):
        t.append(a[i] + b[i])
    return t
        


def solve(times, big, lists, cost):
    if times == N:
        if not len(list(filter(lambda x:x<X, lists))):
            return min(big, cost)
        else:
            return big

    big = solve(times + 1, big, adde(lists, A[times]), cost + C[times])
    big = solve(times + 1, big, lists, cost)
    
    return big

ans = solve(0, float('inf'), [0 for i in range(M)], 0)
print(ans if ans != float('inf') else -1)
