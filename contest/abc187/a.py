def s(a):
    tmp = 0
    for i in a:
        tmp += int(i)
    return tmp

a, b = input().split()
print(max(s(a), s(b)))
