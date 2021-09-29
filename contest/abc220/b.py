def k_to_ten(num, k):
    ret = 0
    
    for i, keta in enumerate(num[::-1]):
        ret += k**i * int(keta)
    return ret

k = int(input())
a, b = input().split()

print(k_to_ten(a, k) * k_to_ten(b, k))
