global A, B
A, B, N = map(int, input().split())

def f(num):
    return(A * num) // B - A * (num // B)

print(f(min(B - 1, N)))
