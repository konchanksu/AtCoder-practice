import heapq

Q = int(input())
add = 0
array = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(array, query[1] - add)
    elif query[0] == 2:
        add += query[1]
    else:
        print(heapq.heappop(array) + add)
