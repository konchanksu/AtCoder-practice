N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in A:
    if i <= 10:
        continue
    ans += i-10
print(ans)
