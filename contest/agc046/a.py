import math
import time

X = int(input())
K = 0
a = X
E = 0.1 ** 5

now = [0.0, 0.0]
while True:
    if now[0] <= E and now[0] >= -E and now[1] >= -E and now[1] <= E and K:
        print(K)
        break

    now[0] += math.cos(math.radians(a))
    now[1] += math.sin(math.radians(a)) 

    a += X
    K += 1        
