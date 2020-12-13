S = input()
length = len(S)
double = [[None for j in range(length)] for i in range(334)]

for i in range(length):
    double[0][i] = i-1 if S[i] == "L" else i+1

for i in range(1, 333):
    for j in range(length):
        double[i][j] = double[i-1][double[i-1][j]]

tmp = 10**100
t = []
while tmp:
    t.append(tmp % 2)
    tmp //= 2

count = [0 for i in range(length)]
for i in range(length):
    ans = i
    for j in range(len(t)):
        if t[j]:
            ans = double[j][ans]
    count[ans] += 1
[print(i, end=" ") for i in count]
print()
