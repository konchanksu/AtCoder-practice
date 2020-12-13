n = int(input())
s = []
for i in range(n):
    s.append(input())

dicts = {}
for i in s:
    if i not in dicts:
        dicts[i] = 1
    else:
        dicts[i] += 1

max_v = max(dicts.values())
a = [k for k, v in dicts.items() if v == max_v]
b = sorted(a)
[print(i) for i in b]
