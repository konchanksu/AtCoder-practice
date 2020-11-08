K = int(input())
S = input()

print(S[0:K] + '...' if K < len(S) else S)
