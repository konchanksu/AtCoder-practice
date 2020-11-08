N = input()

tmp = []
ans = 0

for n in N:
    ans += (int(n) % 3)
    tmp.append(int(n) % 3)

if ans % 3 == 0:
    print(0)
elif ans % 3 == 1:
    if len(N) > 1 and 1 in tmp:
        print(1)
    elif len(N) > 2:
        k = 0
        for i in tmp:
            if i == 2:
                k += 1
        if k > 1:
            print(2)
        else:
            print(-1)
    else:
        print(-1)
else:
    if len(N) > 1 and 2 in tmp:
        print(1)
    elif len(N) > 2:
        k = 0
        for i in tmp:
            if i == 1:
                k += 1
        if k > 1:
            print(2)
        else:
            print(-1)
    else:
        print(-1)