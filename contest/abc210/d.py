H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# A[H-1][W-1]
ans = float("inf")
l_cost = [A[0][0]]
r_cost = [0]*(W-1) + [A[0][W-1]]

for w in range(1, W):
    if l_cost[-1]+C >= A[0][w]:
        l_cost.append(A[0][w])
    else:
        l_cost.append(l_cost[-1]+C)

now = W-1
for w in range(W-2, -1, -1):
    if r_cost[now]+C >= A[0][w]:
        r_cost[w] = A[0][w]
    else:
        r_cost[w] = r_cost[now]+C
    now -= 1

for w in range(1, W):
    ans = min(ans, l_cost[w-1]+A[0][w]+C)

for h in range(1, H):
    for w in range(W):
        ans = min(ans, l_cost[w]+C+A[h][w], r_cost[w]+C+A[h][w])
        if l_cost[w]+C >= A[h][w]:
            l_cost[w] = A[h][w]
        else:
            l_cost[w] += C
        if r_cost[w]+C >= A[h][w]:
            r_cost[w] = A[h][w]
        else:
            r_cost[w] += C
    
    for w in range(1, W):
        if l_cost[w-1]+C < l_cost[w]:
            l_cost[w] = l_cost[w-1]+C
    
    for w in range(W-2, -1, -1):
        if r_cost[w+1]+C < r_cost[w]:
            r_cost[w] = r_cost[w+1]+C

    for w in range(1, W):
        ans = min(ans, l_cost[w-1]+A[h][w]+C)

print(ans)
