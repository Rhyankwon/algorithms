import collections

N, T = map(int, input().split())
signs = collections.defaultdict(list)
inter = {1: ['up', 'down', 'right'] , 2: ['left', 'up', 'right'], 3: ['left', 'up', 'down'],\
           4: ['left', 'down', 'right'], 5: ['up', 'right'], 6: ['left', 'up'], 7: ['left', 'down'],\
           8: ['down', 'right'], 9: ['down', 'right'], 10: ['up', 'right'], 11: ['left', 'up'],\
           12: ['left', 'down']}  #신호등 설정
direction_info = {'left' : [0, -1], 'right' : [0, 1], 'up' : [-1, 0], 'down' : [1, 0]}  #각 신호에 따라 좌표 이동
for i in range(N):
    for j in range(N):
        signs[i, j].extend(list(map(int, input().split())))
stack = []
stack.append([[0, 0], 0, 'up'])  #시작지점

result = set()

def is_not_out(index):
    if index[0]<0 or index[0]>(N-1) or index[1]<0 or index[1]>(N-1):  #좌표 내로만 이동하는지 확인
        return False
    else :
        return True
check = set()
prev_direction = {'up' : [2, 6, 10], 'right' : [1, 5, 9], 'down' : [4, 8, 12], 'left' : [3, 7, 11]}  #이전 방향에 따라 사용가능한 신호등 확인
while stack:
    [tmp, time, direction] = stack.pop()
    check.add(tuple([tmp[0], tmp[1], time%4, direction]))
    result.add(tuple(tmp))
    ops = inter[signs[tuple(tmp)][time%4]]
    if signs[tuple(tmp)][time%4] not in prev_direction[direction]:
        continue
    for op in ops:
        i = direction_info[op]
        cur = [tmp[0]+i[0], tmp[1]+i[1]]
        if is_not_out(cur) and (time+1) <= T and (tuple([cur[0], cur[1], (time+1)%4, op]) not in check):
            stack.append([cur, time+1, op])

print(len(set(result)))