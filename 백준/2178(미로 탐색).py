import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(input().strip()) for i in range(N)]

start = [1, 0, 0]
end = [N-1, M-1]

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

stack = [start]
grid[0][0] = 0

answer = []
while stack:
    tmp = heapq.heappop(stack) #거리 짧은 순서로 스택 순회
    [num, r, c] = tmp
    for dx, dy in d:
        nx, ny = r + dx, c + dy
        if nx >= 0 and nx < N and ny >= 0 and ny < M and grid[nx][ny] == '1':
            if [nx, ny] == end:
                answer.append(num+1) #어차피 매번 최소 num 선택이라 여기서 그냥 출력하고 끝내도 ok
            else:
                grid[nx][ny] = '0'
                heapq.heappush(stack, [num+1, nx, ny])

print(min(answer))