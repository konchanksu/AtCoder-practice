A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

tmp = A - B if A > B else B - A 

print('YES' if tmp <= (V - W) * T else 'NO')
