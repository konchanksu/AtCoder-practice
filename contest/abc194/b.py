n = int(input())
person = [list(map(int, input().split())) for _ in range(n)]

a = float("inf")
for i in range(n):
    for j in range(n):
        if i == j:
            a = min(person[i][0] + person[j][1], a)
        else:
            a = min(max(person[i][0], person[j][1]), a)
print(a)
