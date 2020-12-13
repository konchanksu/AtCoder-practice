N = int(input())

A = list(map(lambda x:int(x)-1, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
before = -10
for i in A:
    ans += B[i]
    if i - before == 1:
        ans += C[before]
    before = i

print(ans)
