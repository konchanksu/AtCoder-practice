N = int(input())
A = list(map(int, input().split()))
now = 0

for a in A:
    if now+1 == a:
        now += 1

print(N - now if now else -1)
