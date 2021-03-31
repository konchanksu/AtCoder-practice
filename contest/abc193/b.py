n = int(input())

ans = float("inf")
for _ in range(n):
    a, p, x = map(int, input().split())
    if a >= x:
        continue
    ans = min(ans, p)

print(ans if ans != float("inf") else -1)
