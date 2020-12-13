N, X = map(int, input().split())
S = input()

for i in S:
    if X != 0 and i == "x":
        X -= 1
    elif i == "o":
        X += 1
        
print(X)
