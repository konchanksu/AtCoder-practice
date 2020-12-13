from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
count_s = []
for s in S:
    tmp = 0
    if len(list(filter(lambda x: s[0], s))) == 1:
        continue
    for word in s:
        tmp += 10 ** (ord(word) - ord("a"))
    count_s.append(tmp)

pattern = Counter(count_s)
ans = 0
for i in pattern.values():
    ans += (i*(i-1)) // 2
print(ans)
