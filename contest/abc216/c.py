N = int(input())
ans = ""

while N:
    if N % 2 == 0:
        N //= 2
        ans += "B"
    else:
        N -= 1
        ans += "A"

print(ans[::-1])
