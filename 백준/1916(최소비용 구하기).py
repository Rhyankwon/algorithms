import sys
import collections
import heapq

input = sys.stdin.readline

routes = collections.defaultdict(list)

N = int(input())
M = int(input())

visited = [sys.maxsize for i in range(N+1)]

for i in range(M):
    v1, v2, c = map(int, input().split())
    routes[v1].append([c, v2])

s, e = map(int, input().split())

stack = [[0, s]]
visited[s] = 0

while stack:
    c, v = heapq.heappop(stack)
    for i in routes[v]:
        if visited[i[1]] > i[0]+c:
            visited[i[1]] = i[0]+c
            heapq.heappush(stack, [i[0]+c, i[1]])
    if v == e:
        print(c)
        break