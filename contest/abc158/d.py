s = input()
q = int(input())
Flag = False
right=''
left=''

for i in range(q):
    t = input()
    if t[0] == '1':
        Flag = not Flag
    else:
        _, f, c = t.split()
        if Flag == False and f == '2' or Flag == True and f == '1':
            right += c
        else:
            left += c

ans = left[::-1] + s + right
print(ans if not Flag else ans[::-1])
