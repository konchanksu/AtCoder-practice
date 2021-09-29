A = list(map(int, input().split()))

for a in A:
    print(chr(ord("a")-1 + a), end="")
print()
