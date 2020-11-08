MOD = 10 ** 9 + 7
for _ in range(int(input())):
    N, A, B = map(int, input().split())

    pt = (pow((N - A + 1), 2, MOD) * pow((N - B + 1), 2, MOD)) % MOD

    for i in range((N + 1) // 2):
        t = ((N - i * 2) - A) * 4
        if t < 0:
            break
        elif t == 0:
            t = 1

        