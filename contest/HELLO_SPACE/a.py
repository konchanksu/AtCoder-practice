S = input()
ans = 0

for i in range(len(S)-3):
    if "ZONe" == S[i:i+4]:
        ans += 1
print(ans)
