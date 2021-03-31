def max_num(num):
    return int("".join(sorted(str(num), reverse=True)))
    
def min_num(num):
    return int("".join(sorted(str(num))))

n, k = map(int, input().split())

for i in range(k):
    n = max_num(n) - min_num(n)

print(n)
