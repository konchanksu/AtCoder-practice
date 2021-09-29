def tmp(S):
    w = []
    h = []
    for i, s in enumerate(S):
        if list(filter(lambda x: x!=".", s)):
            w.append(i)
            break
    for i, s in enumerate(S[::-1]):
        if list(filter(lambda x: x!=".", s)):
            w.append(len(S)-i)
            break

    for i in range(len(S)):
        if list(filter(lambda x: x!=".", [aaa[i] for aaa in S])):
            h.append(i)
            break
    for i in range(len(S)-1, -1, -1):
        if list(filter(lambda x: x!=".", [aaa[i] for aaa in S])):
            h.append(i+1)
            break
    
    return (w, h)

def turn(A):
    ans = [[] for _ in range(len(A[0]))]
    for a in A[::-1]:
        for i, s in enumerate(a):
            ans[i].append(s)
    return ans

def equal(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    return True


    
N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

ns = []
nt = []

w, h = tmp(S)
for i in range(*w):
    ns.append([])
    for j in range(*h):
        ns[-1].append(S[i][j])

w, h = tmp(T)
for i in range(*w):
    nt.append([])
    for j in range(*h):
        nt[-1].append(T[i][j])

ans = False
for i in range(4):
    if equal(ns, nt):
        ans = True
        break
    nt = turn(nt)

print("Yes" if ans else "No")
