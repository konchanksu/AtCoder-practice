k, x = map(int, input().split())
small = -1000000
big = 1000000

for i in range(max(small, x-k+1), min(big, x+k-1)+1):
    print(i, end=" ")
print()
