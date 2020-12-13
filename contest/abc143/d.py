n = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0

sets = set()
for i in range(n):
    l = L[i]
    for j in L[i+1:]:
        sets.add((l, j))

TFline = [False for i in range(10**3 + 1)]
Numline = [0 for i in range(10**3 + 1)]
for l in L:
    TFline[l] = True
    if Numline[l] < 3:
        Numline[l] += 1

TNumLine = [0]
for i in range(1, 10**3 + 1):
    TNumLine.append(TNumLine[-1] + 1 if TFline[i] else TNumLine[-1])

for lines in sets:
    minline = min(lines)
    maxline = max(lines)
    if not abs(minline - maxline):
        if Numline[minline] == 3:
            ans += 1
        ans += TNumLine[minline-1] - TNumLine[min(abs(minline - maxline), minline-1)]
    else:
        if Numline[minline] >= 2 and abs(minline - maxline) + minline > maxline:
            ans += 1
        ans += TNumLine[minline-1] - TNumLine[min(abs(minline - maxline), minline-1)]
    
print(ans)
