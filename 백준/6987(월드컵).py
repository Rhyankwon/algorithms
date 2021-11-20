import sys

input = sys.stdin.readline

results = []

for i in range(4):
    results.append(list(map(int, input().split())))

def check(former, latter):
    global board
    global answer
    flag = []
    if former == 5:
        if sum(sum(board, [])) == 0:
            answer = 1
            return
    elif latter == 6:
        check(former+1, former+2)
    else:
        if board[former][0] != 0 and board[latter][2] != 0:
            flag.append([0, 2])
        if board[former][1] != 0 and board[latter][1] != 0:
            flag.append([1, 1])
        if board[former][2] != 0 and board[latter][0] != 0:
            flag.append([2, 0])
        for a, b in flag: #여기서 for을 안 쓰면 더 빠르겠지만 보기 더 깔끔.
            board[former][a] -= 1
            board[latter][b] -= 1
            check(former, latter+1)
            board[former][a] += 1
            board[latter][b] += 1

for i in range(4):
    board = [[]for i in range(6)]
    for j in range(6):
        board[j].extend(results[i][3*j:3*j+3])
    answer = 0
    check(0, 1)
    if i != 3:
        print(answer, end = ' ')
    else :
        print(answer)