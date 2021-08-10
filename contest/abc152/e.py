def soinsu(x, p, data):
    for i in p:
        if x==1:
            break
        tmp = 0
        while not x%i:
            tmp += 1
            x //= i
        data[i] = max(data[i], tmp)

def Eratosthenes(n):
    is_prime = [True for i in range(0, n + 1)]
    prime = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n + 1, i):
                is_prime[j] = False
    return prime

N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

prs = Eratosthenes(1000)
data = {i:0 for i in prs}

for a in A:
    soinsu(a, prs, data)

l = 1
for k, v in data.items():
    if not v:
        continue
    l *= k*v
    l %= MOD

ans = 0
for a in A:
    pass

print(l)
