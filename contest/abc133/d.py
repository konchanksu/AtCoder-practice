n = int(input())
a = list(map(int, input().split()))

x = [sum(a[0::2]) - sum(a[1::2])]

for i in range(0, n-1):
    x.append(2*a[i] - x[-1])

print(" ".join(map(str, x)))
