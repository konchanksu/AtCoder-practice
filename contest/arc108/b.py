N = int(input())
S = input()

counter = []
fox = 0

for s in S:
    if s not in ("f", "o", "x"):
        counter = []
    
    if s == "f":
        counter.append("f")

    if s == "o":
        if len(counter) != 0:
            if counter[-1] == "f":
                counter[-1] = "fo"
            else:
                counter = []

    if s == "x":
        if len(counter) != 0:
            if counter[-1] == "fo":
                fox += 3
                counter.pop()
            else:
                counter = []

print(N - fox)
