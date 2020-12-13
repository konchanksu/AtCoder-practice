import bisect

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

for i in range(M):
    now = A.pop() // 2
    bisect.insort_left(A, now)

print(sum(A))
