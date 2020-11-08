d = int(input())

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if d < 10:
    print(d)
    exit()

times = 9

while True:
    tmps = []
    for i in lists:  
        if i % 10 == 0:
            times += 2
            tmps.append(i * 10)
            tmps.append(i * 10 + 1)
            
        elif i % 10 == 9:
            times += 2
            tmps.append(i * 10 + 8)
            tmps.append(i * 10 + 9)
            
        else:
            times += 3
            tmps.append(i * 10 + (i % 10 - 1))
            tmps.append(i * 10 + (i % 10))
            tmps.append(i * 10 + (i % 10 + 1))
        
        if times >= d:
            print(tmps[len(tmps) - abs(times - d) - 1])
            exit()
            
    lists = tmps
