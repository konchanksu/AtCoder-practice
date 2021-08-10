N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
bunkai = [A[0]]

for i in range(1, N):
    bunkai.append(A[i]-A[i-1])
bunkai.append(L-A[-1])

ok, ng = 0, L
while abs(ok-ng) > 1:
    md = (ok + ng) // 2
    count = 0
    now = 0
    for i in bunkai:
        now += i
        if now >= md:
            now = 0
            count += 1

    if count <= K:
        ng = md
    else:
        ok = md
print(ok)
