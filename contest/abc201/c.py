S = input()
num = []
for s in S:
    if s == 'o':
        num.append(1)
    elif s == 'x':
        num.append(0)
    else:
        num.append(-1)

ans = 0
for i in range(10000):
    Str = str(i).zfill(4)
    tmp = [0 for _ in range(10)]
    for s in Str:
         tmp[int(s)] = 1
    
    a = True
    for j in range(10):
        if num[j] == 0 and tmp[j] == 1 or num[j] == 1 and tmp[j] == 0:
            a = False
            break
    if a:
        ans += 1
print(ans)


