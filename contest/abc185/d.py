N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if M == 0:
    print(1)
else:
    k = A[0] - 1 if A[0] - 1 != 0 else float("inf")
    haba = [] if A[0] - 1 == 0 else [A[0] - 1]
    for i in range(1, M):
        if A[i] - A[i-1] != 1:
            k = min(A[i] - A[i-1] - 1, k)
            haba.append(A[i] - A[i-1] - 1)
    k = min(N - A[-1], k) if N - A[-1] != 0 else k
    if N - A[-1] != 0:
        haba.append(N - A[-1])
    
    ans = 0
    for h in haba:
        if h % k != 0:
            ans += h // k + 1
        else:
            ans += h // k
    print(ans)
