def GCM(a, b):
    if a < b:
        a, b = b, a
    if a % b:
        return GCM(b, a % b)
    return b

def yakusuu(r):
    if r == 1:
        return []
    ret = [r]
    for i in range(2, int(r**0.5)+1):
        if r % i == 0:
            ret.append(i)
            ret.append(r//i)
    return sorted(ret)

a, b = map(int, input().split())
yakusu = yakusuu(GCM(a, b))

ans = []
for i in yakusu:
    tmp = True
    for j in ans:
        if i % j == 0:
            tmp = False
            break
    if tmp:
        ans.append(i)

print(len(ans)+1)
