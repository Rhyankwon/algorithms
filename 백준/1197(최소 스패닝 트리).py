import sys
import collections
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
graph = collections.defaultdict(list)

visited = [False for i in range(V+1)]

for i in range(E):
    v1, v2, c = input().split()
    graph[v1].append([int(c), v2])
    graph[v2].append([int(c), v1])

stack = []

stack.append([0, v1])

sum = 0
cnt = 0
while stack:
    if cnt == V:
        break
    c, v2 = heapq.heappop(stack)
    if visited[int(v2)]:
        continue
    sum += c
    cnt += 1
    visited[int(v2)] = True
    for c, v1 in graph[v2]:
        heapq.heappush(stack, [c, v1])
print(sum)