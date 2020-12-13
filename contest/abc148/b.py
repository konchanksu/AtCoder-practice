n = int(input())
s, t = input().split()
[print(i + j, end='')for i, j in zip(s, t)]
print()
