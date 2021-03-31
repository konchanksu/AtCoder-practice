def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a%b)

N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
all_gcd = A[0]

for a in A[1:]:
    all_gcd = gcd(all_gcd, a)

mul = 1
for a in A:
    mul *= a
    mul %= MOD

print(mul)
