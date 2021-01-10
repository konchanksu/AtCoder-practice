n = int(input())

s = {}
for i in range(n):
    tmp, temp = input().split()
    if tmp not in s.keys():
        s[tmp] = [(i, int(temp))]
    else:
        s[tmp] += [(i, int(temp))]
    
    
s = sorted(s.items(), key=lambda x:x[0])

for i in s:
    a = sorted(i[1], key=lambda x:x[1], reverse=True)
    for j in a:
        print(j[0] + 1)
        
