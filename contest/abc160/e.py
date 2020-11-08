x, y, a, b, c = map(int, input().split())
pa = sorted(list(map(int, input().split())), reverse=True) # 赤
qb = sorted(list(map(int, input().split())), reverse=True) # 緑
rc = list(map(int, input().split())) # 透明

ans = []
ans += pa[:x]
ans += qb[:y]
ans += rc

print(sum(sorted(ans, reverse=True)[:x+y]))
