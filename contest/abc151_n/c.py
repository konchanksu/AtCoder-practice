n, m = map(int, input().split())

ac_check = [False for i in range(n)]
wa_count = [0 for i in range(n)]

clear = 0
error = 0
for i in range(m):
    p, s = input().split()
    p = int(p) - 1

    if s == 'AC' and ac_check[p] == False:
        ac_check[p] = True
        error += wa_count[p]
    elif s == 'WA' and ac_check[p] == False:
        wa_count[p] += 1

for i in range(n):
    if ac_check[i]:
        clear += 1

print(clear, error)
