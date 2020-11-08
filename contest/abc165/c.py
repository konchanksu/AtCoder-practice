global N, M, Q, T
N, M, Q = map(int, input().split())
T = []
for i in range(Q):
    T.append(list(map(int, input().split())))

def score(lists):
    tmp = 0
    for i in T:
        if lists[i[1] - 1] - lists[i[0] - 1] == i[2]:
            tmp += i[3]
    return tmp
        
def make_lists(lists=[], s=0, ans=0, times=0):
    if times == N:
        return score(lists)

    for i in range(s, M):
        ans = max(ans, make_lists(lists + [i], i, ans, times + 1))
    return ans
        
print(make_lists())
