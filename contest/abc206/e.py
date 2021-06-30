def Eratosthenes(n):
    is_prime = [True for i in range(0, n + 1)]
    prime = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n + 1, i):
                is_prime[j] = False
    return prime

l, r = map(int, input().split())

num = 2
ans = 0
prime = Eratosthenes(r)

while True:
    tmp = 0
    v = 0
    a = l // num if l % num == 0 else l // num + 1
    b = r // num

    while True:
        tmp_num = prime[v]
        if a < tmp_num:
            a = tmp_num
        if a == b:
            break
        print(a, b, tmp_num)
        aa = tmp_num - a % tmp_num
        bb = b % tmp_num

        s = aa + bb
        aaa = (a + aa)
        bbb = (b - bb)

        s += (bbb-aaa) - (bbb-aaa) // tmp_num

        if s <= 0:
            break
        tmp += (s-1) * s // 2
        v += 1

    if tmp <= 0:
        break

    ans += tmp
    num += 1

print(ans*2)

