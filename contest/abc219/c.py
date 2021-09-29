x = input()
t_dict = {s:i for i, s in enumerate(x)}
n = int(input())
s = [input() for _ in range(n)]

def sort_key(t_dict, string):
    i = 10
    ans = 0
    for s in string:
        ans += (t_dict[s]+1) * (27 ** i)
        i -= 1
    return ans

s.sort(key=lambda x: sort_key(t_dict, x))
[print(i) for i in s]
