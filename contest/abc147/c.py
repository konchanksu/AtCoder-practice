N = int(input())
talks = [[None for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(int(input())):
        x, y = map(int, input().split())
        x -= 1
        talks[i][x] = y if y == 1 else -1

for tmp in range(2**N - 1, -1, -1):
    Honest = [None for i in range(N)]
    digit = N
    OK = True
    i = tmp
    
    for _ in range(N):
        digit -= 1
        isTalk = i % 2
        if isTalk:
            if Honest[digit] == -1:
                OK = False
                break
            Honest[digit] = 1
            
            for j in range(N):
                if talks[digit][j] and Honest[j]:
                    if talks[digit][j] != Honest[j]:
                        OK = False
                        break
                if talks[digit][j]:
                    Honest[j] = talks[digit][j]

        else:
            if Honest[digit] == 1:
                OK = False
            Honest[digit] = -1
        if not OK:
            break
        i //= 2

    if OK:
        print(len(list(filter(lambda x: x=="1", str(bin(tmp))))))
        break
