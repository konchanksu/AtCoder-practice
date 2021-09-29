N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

dp = [[0 for i in range(10)] for _ in range(N)]
dp[0][A[0]] += 1


for i, a in enumerate(A[1:]):
    for num in range(10):
        expr = (num + a) % 10
        dp[i+1][expr] += dp[i][num]
        dp[i+1][expr] %= MOD
        
        expr = (num * a) % 10
        dp[i+1][expr] += dp[i][num]
        dp[i+1][expr] %= MOD
        
[print(i) for i in dp[N-1]]
