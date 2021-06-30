from math import factorial

def A(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

def rec(string, a, b, k):
    if a+b == 0:
        return string
    if b == 0:
        return string + "a"*a
    if a == 0:
        return string + "b"*b
    tmp = A(a+b-1, a-1)
    if k > tmp:
        return rec(string+"b", a, b-1, k-tmp)
    else:
        return rec(string+"a", a-1, b, k)
        
        

a, b, k = map(int, input().split())
print(rec("", a, b, k))
