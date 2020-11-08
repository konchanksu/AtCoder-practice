s, t = input().split()
a, b = map(int, input().split())
dicts = {}
dicts[s], dicts[t] = a, b
u = input()
dicts[u] -= 1
print(dicts[s], dicts[t])
