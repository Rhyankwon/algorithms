N = int(input())

strs = list(input())
signal = []

for i in range(5):
    signal.append(strs[((i*N)//5):(((i+1)*N)//5)])

template = [[]for i in range(5)]
for j in range(3):
    for i in range(5):
        if i in [1, 3] and j in [1]:
            template[i].append('.')
        else:
            template[i].append('#')

def check(board):
    difference = []
    for i in range(5):
        for j in range(3):
            if template[i][j] != board[i][j]:
                difference.append([i, j])
    if [0, 1] in difference and [2, 1] in difference:
        return 1
    elif difference == [[1, 0], [3, 2]]:
        return 2
    elif difference == [[1, 0], [3, 0]]:
        return 3
    elif difference == [[0, 1], [3, 0], [4, 0], [4, 1]]:
        return 4
    elif difference == [[1, 2], [3, 0]]:
        return 5
    elif difference == [[1, 2]]:
        return 6
    elif difference == [[1, 0], [2, 0], [2, 1], [3, 0], [4, 0], [4, 1]]:
        return 7
    elif template == board:
        return 8
    elif difference == [[3, 0]]:
        return 9
    else:
        return 0

answer = ''

j = 0
while j < N//5:
    single = [[]for i in range(5)]
    tmp = 0
    if signal[0][j] == '#':
        for i in range(5):
            single[i].extend(signal[i][j:j+3])
            single[i].extend(['.'] * (3 - len(single[i])))
        tmp = check(single)
        answer += str(tmp)
        if tmp == 1:
            j += 2
        else:
            j += 4
    else :
        j += 1

print(answer)