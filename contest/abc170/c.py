X, N = map(int, input().split())
if N == 0:
    print(X)
    exit()

p = list(map(int, input().split()))

tmp = -1
for i in range(-1, 110):
    if i not in p:
        tmp = i if abs(X - tmp) > abs(X - i) else tmp
    
print(tmp)
