N = int(input())
A = list(map(int, input().split()))

if N == 0:
    print(A[0] if A[0] <= 1 else -1)
    exit()

if A[0] and N >= 1:
    print(-1)
    exit()

# 根の数
node = 1
root = 0

s = sum(A)

for i in range(len(A) - 1):
    node = min(s, node * 2) - A[i + 1]
    
    if node < 0:
        print(-1)
        exit()
    
    s -= A[i + 1]
    root += node

print(root + sum(A) + 1 if not node else -1)

