def evaluate(num1, num2):
    diff = num2 - num1 + 1
    return num1 * diff + (diff - 1) * diff // 2

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
sabun = []
for i in range(1, N):
    sabun.append(A[i-1] - A[i])
sabun.append(A[-1])

if sum(A) <= K:
    ans = 0
    for a in A:
        ans += (a+1) * a // 2
    print(ans)
else:
    ans = 0
    tmp = 1
    while K > 0:
        if sabun[tmp-1] * tmp <= K:
            ans += tmp * evaluate(A[tmp]+1, A[tmp-1])
            K -= sabun[tmp-1] * tmp
        else:
            a = K // tmp
            b = K % tmp
            ans += tmp * evaluate(A[tmp-1]-a+1, A[tmp-1])
            ans += b * (A[tmp-1]-a)
            break
        tmp += 1
    print(ans)
