Sx, Sy, Gx, Gy = map(int, input().split())

if Sx > Gx:
    Sx, Sy, Gx, Gy = Gx, Gy, Sx, Sy

tmp = Gx - Sx

print(Sx + tmp * Sy / (Sy + Gy))
