N = int(input())
A = list(map(int, input().split()))
tmp = A[0]

for i in range(1, len(A)):
    tmp = tmp ^ A[i]
    
for i in A:
    print(tmp ^ i, end=' ')
print()
