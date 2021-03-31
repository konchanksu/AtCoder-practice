def Eratosthenes(n):
    is_prime = [True for i in range(0, n + 1)]
    prime = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n + 1, i):
                is_prime[j] = False
    return prime + [n]

def all(now, addr, ret):
    global prime
    for i in range(now+1, len(prime)):
        all(i, addr*prime[i], ret)
    ret.append(addr)
    return ret

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        if b == 1:
            return True
        return False
    return gcd(b, a%b)

n = int(input())
x = list(map(int, input().split()))
prime = Eratosthenes(50)

a = sorted(all(-1, 1, []))

for i in a[1:]:
    if not tuple(filter(lambda x:gcd(i, x), x)):
        break
print(i)
