def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
    
def mod_inv(a, m):
    x = extgcd(a, m)[1]
    return x % m

for _ in range(int(input())):
    N, S, K = map(int, input().split())
    S = N - S
    d = gcd(gcd(N, S), K)
    N, S, K = N // d, S // d, K // d
    if gcd(N, K) != 1:
        print(-1)
    else:
        a = (mod_inv(K, N) * S) % N
        print(a)
        
