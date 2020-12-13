N = int(input())
t = input()

if t == "1":
    print(2 * 10**10)
elif t == "0":
    print(10**10)
elif t == "11":
    print(10**10)
else:
    ans = True
    tmp = 1
    if t[0] == "0":
        for i, s in enumerate(t):
            if i % 3 == 1:
                tmp += 1
            if i % 3 == 0 and s == "1":
                ans = False
            elif i % 3 != 0 and s == "0":
                ans = False
            
    elif t[0:2] == "10":
        for i, s in enumerate(t[1:]):
            if i % 3 == 1:
                tmp += 1
            if i % 3 == 0 and s == "1":
                ans = False
            elif i % 3 != 0 and s == "0":
                ans = False

    elif t[0:3] == "110":
        for i, s in enumerate(t[2:]):
            if i % 3 == 1:
                tmp += 1
            if i % 3 == 0 and s == "1":
                ans = False
            elif i % 3 != 0 and s == "0":
                ans = False
    else:
        ans = False
    
    if not ans:
        print(0)
    else:
        print(10**10-tmp+1)
