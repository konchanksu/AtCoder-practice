S = input()
T = input()
ans = float('inf')

for i in range(0, len(S) - len(T) + 1):
    tmp = len(T)
    for j in range(0, len(T)):
        if T[j] == S[i + j]:
            tmp -= 1
    ans = min(tmp, ans)

print(ans)
