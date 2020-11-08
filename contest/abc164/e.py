N, M, S = map(int, input().split())
U, V, A, B = [], [], [], []
for i in range(M):
    t, e, m, p = map(int, input().split())
    U.append(t), V.append(e), A.append(m), B.append(p)
C, D = [], []
for i in range(N):
    t, e = map(int, input().split())
    C.append(t), D.append(e)
