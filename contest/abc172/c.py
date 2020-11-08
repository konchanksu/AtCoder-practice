N, M ,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ruiA, ruiB = [0], [0]

for i in range(N):
    ruiA.append(ruiA[i] + A[i])

for j in range(M):
    ruiB.append(ruiB[j] + B[j])

t = False
for i in range(N + M + 1):
    if i <= N and ruiA[i] <= K:
        continue
    if i <= M and ruiB[i] <= K:
        continue
    if i > N and ruiA[N] + ruiB[i - N] <= K:
        continue
    if i > M and ruiA[i - M] + ruiB[M] <= K:
        continue

    t = False
    for j in range(0, i + 1):
        if j > M or i - j > N:
            continue
        if ruiA[i - j] + ruiB[j] <= K:
            t = True
            break

    if not t:
        print(i - 1)
        exit()

print(N + M)
