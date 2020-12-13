a, b = map(int, input().split())

def ccc(a, b):
    if a % b == 0:
        return b
    return ccc(b, a % b)

print(a * b // ccc(a, b))
