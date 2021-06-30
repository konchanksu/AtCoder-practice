s1 = input()
l1 = len(s1)
s2 = input()
l2 = len(s2)
s3 = input()
l3 = len(s3)

if not (l3 - max(l1, l2) in (1, 0)):
    print("UNSOLVABLE")
else:
    
