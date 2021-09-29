def Eratosthenes(n):
    is_prime = [True for i in range(0, n + 1)]
    prime = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n + 1, i):
                is_prime[j] = False
    return prime

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = set(A)

ans = [True for i in range(0, M+1)]
ans[0] = False
primes = Eratosthenes(M+1)

for p in primes:
    for a in A:
        if not a % p:
            for j in range(p, M+1, p):
                ans[j] = False
            break

print(len(tuple(filter(lambda x: x, ans))))

for i in range(1, M+1):
    if ans[i]:
        print(i)
