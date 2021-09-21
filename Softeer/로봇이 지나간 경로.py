rows, cols = map(int, input().split())
paths = [list(input()) for _ in range(rows)]

def is_path(row, col):
    if row>=0 and row<rows and col>=0 and col<cols:
        return paths[row][col] == '#'
    else :
        return False
directions = ''
stack = []
order = 'A'
flag = 0
for i in range(rows):
    for j in range(cols):
        if paths[i][j] == '#':
            a = is_path(i-1, j)
            b = is_path(i+1, j)
            c = is_path(i, j-1)
            d = is_path(i, j+1)
            if a+b+c+d == 1:
                start = [i,j]
                stack.append([i,j])
                paths[i][j] = '.'
                flag = 1
                if a:
                    directions += '^'
                elif b:
                    directions += 'v'
                elif c:
                    directions += '<'
                elif d :
                    directions += '>'
                break
    if flag == 1:
        break

while stack:
    tmp = stack.pop()
    if directions[-1] == '^':
        for i in range(2):
            tmp[0] -= 1
            paths[tmp[0]][tmp[1]] = '.'
    elif directions[-1] == 'v':
        for i in range(2):
            tmp[0] += 1
            paths[tmp[0]][tmp[1]] = '.'
    elif directions[-1] == '>':
        for i in range(2):
            tmp[1] += 1
            paths[tmp[0]][tmp[1]] = '.'
    elif directions[-1] == '<':
        for i in range(2):
            tmp[1] -= 1
            paths[tmp[0]][tmp[1]] = '.'
    stack.append(tmp)
    i, j = tmp[0], tmp[1]
    if is_path(i-1, j):
        directions += '^'
    elif is_path(i+1, j):
        directions += 'v'
    elif is_path(i, j-1):
        directions += '<'
    elif is_path(i, j+1):
        directions += '>'
    else :
        stack.pop()
tmp_direction = directions[0]
for i in range(1, len(directions)):
    if tmp_direction == directions[i]:
        order += 'A'
    else :
        if tmp_direction == '>':
            if directions[i] == '^':
                order += 'LA'
            elif directions[i] == 'v':
                order += 'RA'
        elif tmp_direction == '<':
            if directions[i] == '^':
                order += 'RA'
            elif directions[i] == 'v':
                order += 'LA'
        elif tmp_direction == '^':
            if directions[i] == '>':
                order += 'RA'
            elif directions[i] == '<':
                order += 'LA'
        elif tmp_direction == 'v':
            if directions[i] == '>':
                order += 'LA'
            elif directions[i] == '<':
                order += 'RA'
    tmp_direction = directions[i]

print(start[0]+1, start[1]+1)
print(directions[0])
print(order)