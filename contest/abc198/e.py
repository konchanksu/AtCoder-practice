N = int(input())

C = list(map(int, input().split()))
move = [[] for _ in range(N)]
ans = [{} for _ in range(N)]

for _ in range(N-1):
    t, m = map(int, input().split())
    move[t-1].append(m-1)
    move[m-1].append(t-1)


