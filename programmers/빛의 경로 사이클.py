import collections

def solution(grid): #미리 L, R, S에 대해 각 방향에서 들어올 때마다 이동 방향 저장
    paths = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    info = {'S' : {(1,0) : [1,0], (-1, 0) : [-1, 0], (0, 1) : [0,1], (0, -1) : [0, -1]}, \
            'L' : {(1,0) : [0,1], (-1, 0) : [0, -1], (0, 1) : [-1,0], (0, -1) : [1, 0]}, \
            'R' : {(1,0) : [0,-1], (-1, 0) : [0, 1], (0, 1) : [1, 0], (0, -1) : [-1, 0]}}

    answer = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for path in paths:
                traced = set()
                num = 0
                stack = [[i, j]+path] #현재 격자 위치와 경로 동시에 저장
                while stack:
                    tmp = stack.pop()
                    if tuple(tmp) in traced: #이미 간 곳이면 pass
                        continue
                    if tuple(tmp) in visited: #이미 탐색한 사이클일 경우 해당 사이클 나가기
                        num = 0
                        break
                    visited.add(tuple(tmp))
                    traced.add(tuple(tmp))
                    cur = tmp[:2]
                    path = tmp[2:]
                    next_block = [(cur[0]+path[0])%len(grid), (cur[1]+path[1])%len(grid[0])]
                    next_path = info[grid[next_block[0]][next_block[1]]][tuple(path)]
                    stack.append(next_block+next_path)
                    num += 1
                if num != 0:
                    answer.append(num)
    return sorted(answer)
