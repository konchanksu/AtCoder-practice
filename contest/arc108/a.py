def yakubun(x):
    ret = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            ret.append([i, x // i])
    return ret

S, P = map(int, input().split())

ans = False
for i in yakubun(P):
    if i[0] + i[1] == S:
        ans = True
        break

print("Yes" if ans else "No")
