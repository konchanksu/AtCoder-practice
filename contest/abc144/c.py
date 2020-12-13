def aaa(n):
    ans = 0
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            ans = [i, n // i]
    return ans
            
n = int(input())
a, b = aaa(n)
print((a - 1) + (b - 1))
