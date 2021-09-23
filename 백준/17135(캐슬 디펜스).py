import itertools
import copy
import sys

N, M, d = map(int, input().split())
grid = [input().split() for i in range(N)]

combs = list(itertools.combinations(range(M), 3)) #가능한 조합 만들기

def find(i, j):
    for k in range(1, d+1): #가까운 거리부터, 왼쪽->오른쪽 순서대로 탐색하다가 1 있으면 탐색 멈추고 리턴
        for l in range(1, k+1):
            if i-l >= 0 and j-(k-l) >= 0: 
                if grid2[i-l][j-(k-l)] == '1':
                    return [i-l, j-(k-l)]
        for l in range(k, 0, -1):
            if i-l >= 0 and j+(k-l) < M:
                if grid2[i-l][j+(k-l)] == '1':
                    return [i-l, j+(k-l)]

answer = -sys.maxsize
for comb in combs:
    num = 0
    grid2 = copy.deepcopy(grid)
    for j in range(N):
        #규칙에 따라 중복된 1을 삭제시킬 수 있으므로 set사용, 지울 인덱스를 먼저 모두 탐색 후 한번에 지우기 
        candidates = set()
        for i in comb:
            candidate = find(N, i)
            if candidate:
                candidates.add(tuple(candidate))
        for candidate in candidates:
            candidate = list(candidate)
            grid2[candidate[0]][candidate[1]] = '0'
            num += 1
        grid2 = [['0' for i in range(M)]] + grid2[:-1]
    answer = max(answer, num)
print(answer)