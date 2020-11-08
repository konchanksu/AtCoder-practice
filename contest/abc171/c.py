N = int(input()) - 1
A = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ans = ''

while True:
    ans += A[N % 26]
    if N < 26:
        break
    N //= 26
    N -= 1 

print(ans[::-1])
