N = int(input())
S = input()
if N % 2:
    print("No")
else:
    print("No" if S[:N//2] != S[N//2:] else "Yes")
