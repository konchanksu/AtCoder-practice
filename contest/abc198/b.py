N = input()
count = 0
count2 = 0

for i in N[::-1]:
    if i != "0":
        break
    count += 1

for i in N:
    if i != "0":
        break
    count2 += 1

if count < count2:
    print("No")
else:
    ans = True
    for i, j in zip(range(count2, len(N)-count), range(len(N)-count-1, count2-1, -1)):
        if N[i] != N[j]:
            ans = False
    print("Yes" if ans else "No")

