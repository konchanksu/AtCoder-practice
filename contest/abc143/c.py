n = int(input())
s = input()

ans = [s[0]]
for i in s[1:]:
    if ans[-1] != i:
        ans.append(i) 
print(len(ans))
