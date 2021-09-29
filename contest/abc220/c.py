N = int(input())
A = list(map(int, input().split()))
X = int(input())

total = sum(A)

ans = (X // total) * len(A)
X -= total * (X // total)

for a in A:
    X -= a
    ans += 1
    if X < 0:
        break

print(ans)
