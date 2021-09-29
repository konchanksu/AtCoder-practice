from collections import Counter

def kaijo(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

S, K = input().split()
K = int(K)
ans = ""

dictionary = Counter(S)
key = sorted(dictionary.keys())

for i in range(len(S)):
    tmp = 0
    for s in key:
        if dictionary[s] == 0:
            continue
        exe = kaijo(len(S)-i-1)
        for k, v in dictionary.items():
            if k == s:
                v -= 1
            if v == 0 or v == 1:
                continue
            else:
                exe //= kaijo(v)
        if exe >= K:
            ans += s
            dictionary[s] -= 1
            break
        else:
            K -= exe

print(ans)
