S = input()

ans = 0
lists = [0 for i in range(2019)]
lists[0] += 1

num = 0
for i in range(len(S) - 1, -1, -1):
    num += pow(10, len(S) - 1 - i, 2019) * int(S[i])
    lists[num % 2019] += 1

for i in range(2019):
    if lists[i] >= 2:
        ans += (lists[i] * (lists[i] - 1)) // 2

print(ans)
