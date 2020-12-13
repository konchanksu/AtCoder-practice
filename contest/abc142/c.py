n = int(input())
a = list(map(int, input().split()))
lists = [i for i in range(1, n + 1)]
dicts = {j:i for i, j in zip(lists, a)}
for i in range(1, n + 1):
    print(dicts[i], end=' ')
print()
