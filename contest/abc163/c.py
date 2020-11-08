n = int(input())
a = list(map(int, input().split()))

dicts = {i:0 for i in range(1, n + 1)}
for i in a:
    dicts[i] += 1

for i in dicts.values():
    print(i)
