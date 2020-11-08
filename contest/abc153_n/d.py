def aaa(hp, times=0):
    if hp == 1:
        return times
    else:
        return aaa(hp//2, times+1)

h = int(input())
ans = 0
for i in range(aaa(h) + 1):
    ans += 2 ** i
print(ans)

