import heapq

N = int(input())

tmp_arr = []
for i in range(N):
    tmp_arr.append(list(input()))

arr = [['#'for i in range(N+2)]for j in range(N+2)]
for i in range(N):
    for j in range(N):
        arr[i+1][j+1] = tmp_arr[i][j]

UP, DOWN, RIGHT, LEFT = [-1, 0], [1, 0], [0, 1], [0, -1]

dir = [DOWN, RIGHT, LEFT, UP]
tmp_dir = [0, 0]
start_cnt = 0
start_point, end_point = [1, 1], [N, N]

start = [start_cnt, start_point, tmp_dir]

heap_list = []
heapq.heappush(heap_list, start)

while heap_list:
    start = heapq.heappop(heap_list)
    cnt, cur, ex_dir = start
    cx, cy = cur
    arr[cx][cy] = '#'
    if [cx, cy] == end_point:
        print(cnt)
        break
        # exit()

    for d in dir:
        dx, dy = d
        nx, ny = cx+dx, cy+dy
        n_cnt = cnt + [1, 0][ex_dir==d]
        if arr[nx][ny] != '#':
            heapq.heappush(heap_list, [n_cnt, [nx, ny], d])
