from collections import Counter
S = input()

if len(S) == 1:
    print('Yes' if int(S) % 8 == 0 else 'No')
elif len(S) == 2:
    print('Yes' if int(S) % 8 == 0 or int(S[1] + S[0]) % 8 == 0 else 'No')
else:
    tmp = Counter(S)
    ans = False
    
    for i in range(0, 1000, 8):
        t = str(i)
        if i < 10:
            t = '00' + t
        elif i < 100:
            t = '0' + t
        x = True
        y = {}
        for j in t:
            if not tmp.get(j):
                x = False
            if y.get(j):
                y[j] += 1
            else:
                y[j] = 1
        if not x:
            continue
        
        if tmp[t[0]] >= y[t[0]] and tmp[t[1]] >= y[t[1]] and tmp[t[2]] >= y[t[2]]:
            ans = True
            break
    
    if ans:
        print('Yes')
    else:
        print('No')
    
