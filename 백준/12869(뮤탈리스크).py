import sys
import itertools
import collections

N = int(input())
scvs = list(map(int, input().split())) + [0] * (3 - N)
visited = [[[0 for i in range(61)]for j in range(61)]for k in range(61)]
answer = sys.maxsize
combs = list(itertools.permutations([9, 3, 1], 3))

q = collections.deque([[scvs, 0]])

while q:
    tmp, cnt = q.popleft()
    check = 0
    for i in range(3):
        if tmp[i] < 0:
            tmp[i] = 0
        if tmp[i] > 0:
            check = 1
    if check == 0:
        break
    for comb in combs:
        next_scv = [0] * 3
        for i in range(3):
            next_scv[i] = [0, tmp[i] - comb[i]][tmp[i] - comb[i]>0]
        if not visited[next_scv[0]][next_scv[1]][next_scv[2]]:
            visited[next_scv[0]][next_scv[1]][next_scv[2]] = 1
            q.append([next_scv, cnt + 1])

print(cnt)