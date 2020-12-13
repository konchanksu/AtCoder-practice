def kaijo(num):
    a = 1
    for i in range(num, 1, -1):
        a *= i
    return a

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

p_len = 0
for i in range(n - 1):
    a = p[i]
    p_len += (len(list(filter(lambda x: x < a, p[i:]))) - 1) * kaijo(n - i - 1)

for i in range(n - 1):
    b = q[i]
    p_len -= (len(list(filter(lambda x: x < b, q[i:]))) - 1) * kaijo(n - i - 1)

print(abs(p_len))

