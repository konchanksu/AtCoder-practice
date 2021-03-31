from math import cos, sin, radians

N = int(input())

x, y = map(int, input().split())
x2, y2 = map(int, input().split())

theta = radians(360 / N)

center = x + (x2 - x) / 2, y + (y2 - y)/2

x -= center[0]
y -= center[1]

ax = cos(theta)*x - sin(theta)*y
ay = sin(theta)*x + cos(theta)*y

ax += center[0]
ay += center[1]

print(ax, ay)


