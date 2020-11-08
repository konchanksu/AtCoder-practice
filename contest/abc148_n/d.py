n = int(input())
a = list(map(int, input().split()))
num = 1
for i in a:
    if i == num:
        num += 1
    
print(len(a) - num + 1 if num != 1 else -1)
