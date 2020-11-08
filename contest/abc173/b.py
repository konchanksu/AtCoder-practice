N = int(input())
S = [input() for i in range(N)]
ans = {'AC':0, 'WA': 0, 'TLE':0, 'RE': 0,}

for i in S:
    ans[i] += 1

for i, j in zip(ans.keys(), ans.values()):
    print(i + ' x ' + str(j))
