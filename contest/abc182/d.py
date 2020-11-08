N = int(input())

A = list(map(int, input().split()))

num = 0
tmp = [0]
nowmax = [0]

for i in A:
    tmp.append(tmp[-1] + i)
    nowmax.append(max(tmp[-1], nowmax[-1]))


k = 0
for i in range(len(tmp)):
    num = max(num, nowmax[i] + k)
    k += tmp[i]
    num = max(k, num)

print(num)
