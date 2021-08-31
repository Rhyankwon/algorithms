def solution(word):
    words = 'AEIOU'
    candidates = []
    def dfs(path):
        if len(path) != 5: #길이 5 이하인 경우만.
            for i in words: #함수 호출할 때마다 모든 단어 반복
                if word not in candidates: #이미 답 찾으면 패스
                    candidates.append(path+i) #아직 답 못찾은경우 후보 리스트에 넣고
                    if path + i == word:  #만약 우리가 원하는 단어 찾으면 재귀 끝내기
                        return
                    else :
                        dfs(path+i)
    dfs('')
    # 답 = 후보 리스트의 길이
    return len(candidates)

import copy

def check(tmp):
    [block, [col_min, row_min], cur] = tmp
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 0:
                i += col_min
                j += row_min
                while i > 0:
                    i -= 1
                    if original_block[i][j] != 0:
                        return False
    return True
def fillzero(tmp):
    [block, [col_min, row_min], cur] = tmp
    for i in range(len(block)):
        for j in range(len(block[0])):
            original_block[i+col_min][j+row_min] = 0
def solution(board):
    global original_board
    original_board = copy.deepcopy(board)
    right_blocks = [[]]
    no_cols = set()
    no_nums = set()
    N = len(board)
    count = 0
    result = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                cur = board[i][j]
                tmp = []
                stack = []
                row_min = col_min = 100
                row_max = col_max = 0
                stack.append([i, j])
                while stack:
                    col, row = stack.pop()
                    if col >= 0 and col < N and row >= 0 and row < N:
                        if board[col][row] == cur:
                            tmp.append([col, row])
                            board[col][row] = 0
                            stack.append([col+1, row])
                            stack.append([col-1, row])
                            stack.append([col, row+1])
                            stack.append([col, row-1])
                for a in tmp:
                    if a[1] in no_cols:
                        continue
                for b in tmp:
                    row_max = max(b[1], row_max)
                    row_min = min(b[1], row_min)
                    col_max = max(b[0], col_max)
                    col_min = min(b[0], col_min)
                block = [row[row_min:row_max+1] for row in original_board[col_min:col_max+1]]
                block_info = [block, [col_min, row_min], cur]
                result.append(block_info)
    answer = 0
    while True:
        count = 0
        for tmp in result:
            if check(tmp):
                fillzero(tmp)
                answer += 1
                count += 1
        if count == 0:
            break                
    return count - len(no_nums)
