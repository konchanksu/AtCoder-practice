n, k, c = map(int, input().split())
s = input()

l_list, r_list = [], []
tmp = 0
b = 0

for i in range(len(s)):
    if s[i] == 'o' and b == 0 and tmp < k:
        l_list.append(i)
        tmp += 1
        b = c
    
    elif b > 0:
        b -= 1

tmp = 0
b = 0

for i in range(len(s) - 1, -1, -1):
    if s[i] == 'o' and b == 0 and tmp < k:
        r_list.append(i)
        tmp += 1
        b = c
        
    elif b > 0:
        b -= 1

for i in range(k):
    if r_list[k - i - 1] == l_list[i]:
        print(l_list[i] + 1)
