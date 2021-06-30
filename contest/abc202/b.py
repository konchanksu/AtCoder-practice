S = input()

for s in S[::-1]:
    if s == "6":
        s = "9"
    elif s == "9":
        s = "6"
    
    print(s, end="")
print()
