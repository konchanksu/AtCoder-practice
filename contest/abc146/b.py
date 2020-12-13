N = int(input())
for s in input():
    print(chr(ord(s) + N) if ord(s) + N <= ord("Z") else chr(ord(s) + N-26) , end="")
print()