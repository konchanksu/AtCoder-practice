import bisect

N, M = map(int, input().split())
H = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))

patA = []
patB = []

for i in range(0, N - 1, 2):
    patA.append(H[i + 1] - H[i])
    patB.append(H[i + 2] - H[i + 1])

patruisekiA = [0]
patruisekiB = [0]

for i in range(len(patA)):
    patruisekiA.append(patruisekiA[-1] + patA[i])
    patruisekiB.append(patruisekiB[-1] + patB[len(patB) - i - 1])

patruisekiA.append(0)
patruisekiB.append(0)

ans = float('inf')
for w in W:
    tmp = bisect.bisect_left(H, w)
    tans = 0
    
    tans += H[tmp] - w if tmp % 2 == 0 else w - H[tmp - 1]
    
    tans += patruisekiA[tmp // 2]
    tans += patruisekiB[(N - tmp) // 2]
    

    ans = min(tans, ans)
    
print(ans)

