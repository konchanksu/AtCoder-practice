N = int(input())
ans = []

for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:  
        ans += [i, N // i]

for a in sorted(set(ans)):
    print(a)

