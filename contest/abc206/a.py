n = int(input())

teika = 206

n *= 1.08
n = int(n)

if n > teika:
    print(":(")
elif n == teika:
    print("so-so")
else:
    print("Yay!")
