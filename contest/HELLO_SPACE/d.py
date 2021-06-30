from collections import deque

S = input()
string = deque()
r = False

for s in S:
    if s == "R":
        r = not r
 
    else:
        if r:
            if not len(string):
                string.append(s)
            elif string[0] == s:
                string.popleft()
            else:
                string.appendleft(s)
        else:
            if not len(string):
                string.append(s)
            elif string[-1] == s:
                string.pop()
            else:
                string.append(s)
 
print("".join(string)[::-1] if r else "".join(string))
