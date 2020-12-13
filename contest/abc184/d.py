a, b, c = map(int, input().split())

dp = [[[0 for i in range(101)] for j in range(101)] for k in range(101)]
dp[a][b][c] = 1
ans = 0

for i in range(0, 298 - a - b - c):
    for A in range(a, min(100, a + i) + 1):
        for B in range(b, min(100, b + i) + 1):
            C = c + i - (A-a) - (B-b)
            if A >= 100 or B >= 100 or C >= 100:
                continue
            
            if A == 99:
                ans += (i+1) * dp[A][B][C] * (99) / (A+B+C)
            else:
                dp[A+1][B][C] += dp[A][B][C] * (A) / (A+B+C)
                
            if B == 99:
                ans += (i+1) * dp[A][B][C] * (99) / (A+B+C)
            else:
                dp[A][B+1][C] += dp[A][B][C] * (B) / (A+B+C)
                
            if C == 99:
                ans += (i+1) * dp[A][B][C] * (99) / (A+B+C)
            else:
                dp[A][B][C+1] += dp[A][B][C] * (C) / (A+B+C)
print(ans)
