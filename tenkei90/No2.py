N = int(input())
ans = []

if not N % 2:
    for i in range(2**N):
        left, right = 0, 0
        s = ""
        for j in range(N-1, -1, -1):
            if i&1<<j:
                s += ")"
                right += 1
                if right > left:
                    s = None
                    break
            else:
                s += "("
                left += 1
                if left > N // 2:
                    s = None
                    break
        if s:
            ans.append(s)

[print(s) for s in ans]
