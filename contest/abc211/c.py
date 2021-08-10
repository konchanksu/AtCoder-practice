s = input()
MOD = 10**9 + 7

chokudai_str = "chokudai"
bef = {chokudai_str[i+1]:chokudai_str[i] for i in range(len(chokudai_str)-1)}
chokudai = {i:0 for i in chokudai_str}

for i in s:
    if i not in chokudai_str:
        continue
    if i == "c":
        chokudai[i] += 1
    else:   
        chokudai[i] += chokudai[bef[i]]
        chokudai[i] %= MOD

print(chokudai["i"])
