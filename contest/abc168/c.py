from math import sin, cos, pi
A, B, H, M = map(int, input().split())

Ax, Ay = cos(M / 30 * pi) * A, sin(M / 30 * pi) * A
Bx, By = cos((M + H * 60) / 360 * pi) * B, sin((M + H * 60) / 360 * pi) * B

print(((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5)
