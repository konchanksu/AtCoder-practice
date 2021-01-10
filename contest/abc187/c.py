N = int(input())

S = [input() for i in range(N)]
str_dict = {}
no = True
for s in S:
    bikkuri = False
    if s[0] == "!":
        s = s[1:]
        bikkuri = True

    if s not in str_dict:
        str_dict[s] = bikkuri
    else:
        if str_dict[s] != bikkuri:
            print(s)
            no = False
            break
if no:
    print("satisfiable")
