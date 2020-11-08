S = int(input())
MOD = 10 ** 9 + 7
if S < 3:
    print(0)

else:
    dp = [0 for i in range(S + 1)]
    dp[0] = 1

    for i in range(3, S + 1):
        dp[i] = sum(dp[: i - 2]) % MOD

    print(dp[S])
