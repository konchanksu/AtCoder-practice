N, D, H = map(int, input().split())
tower = [list(map(int, input().split())) for _ in range(N)]
high = 0

for d, h in tower:
    katamuki = (H - h) / (D - d)
    high = max(high, h - (H - h) * d / (D - d))

print(high)
