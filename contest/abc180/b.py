N = int(input())
A = list(map(int, input().split()))

print(sum(map(abs, A)))
print(sum(map(lambda x: x ** 2, A)) ** 0.5)
print(max(map(abs, A)))
