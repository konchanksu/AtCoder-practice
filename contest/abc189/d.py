N = int(input())
S = [input() for _ in range(N)]
now = N
yes = 0
no = 0

for s in S[::-1]:
    if s == "OR":
        yes += 2 ** now
    else:
        no += 2 ** now
    now -= 1
print(yes + 1)
    