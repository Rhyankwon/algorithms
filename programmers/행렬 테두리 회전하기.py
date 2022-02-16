def solution(rows, columns, queries):
    total = rows*columns
    grid = [[0 for i in range(columns)]for j in range(rows)]
    for i in range(total):
        grid[i//columns][i%columns] = i+1
    answer = []
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for q in queries:
        [f_r, f_c, s_r, s_c] = q
        stack = []
        traced = []
        stack.append([f_r, f_c])
        tmp_value = grid[f_r-1][f_c-1]
        min_value = 10001
        while stack:
            tmp = stack.pop()
            flag = 0
            for dr in d:
                new_tmp = [tmp[0]+dr[0], tmp[1]+dr[1]]
                if new_tmp[0] == f_r or new_tmp[0] == s_r:
                    if s_c >= new_tmp[1] >= f_c:
                        pass
                    else :
                        continue
                elif new_tmp[1] == f_c or new_tmp[1] == s_c:
                    if s_r >= new_tmp[0] >= f_r:
                        pass
                    else :
                        continue
                else :
                    continue
                if new_tmp not in traced:
                    stack.append(new_tmp)
                    flag = 1
                    break
                else :
                    pass
            if flag != 1:
                continue
            traced.append(new_tmp)
            if new_tmp[1] == f_c-1:
                break
            else :
                new_tmp_value = grid[new_tmp[0]-1][new_tmp[1]-1]
                grid[new_tmp[0]-1][new_tmp[1]-1] = tmp_value
                tmp_value = new_tmp_value
            tmp = new_tmp
            min_value = min(min_value, grid[new_tmp[0]-1][new_tmp[1]-1])
        answer.append(min_value)

    return answer
