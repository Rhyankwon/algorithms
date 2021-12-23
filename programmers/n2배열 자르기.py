def solution(n, left, right):
    answer = []
    left_row, left_col = left//n, left%n
    right_row, right_col = right//n, right%n
    for i in range(left_row, right_row+1):
        for j in range(n):
            if left_row == right_row: #예외처리
                if right_col >= j >= left_col:
                    if j <= left_row:
                        answer.append(left_row+1)
                    else :
                        answer.append(j+1)
            else:
                if i == left_row:
                    if j >= left_col:
                        if j <= left_row:
                            answer.append(left_row+1)
                        else :
                            answer.append(j+1)
                elif i == right_row:
                    if j <= right_col:
                        if j <= right_row:
                            answer.append(right_row+1)
                        else :
                            answer.append(j+1)
                else :
                    if j <= i:
                        answer.append(i+1)
                    else :
                        answer.append(j+1)
    return answer