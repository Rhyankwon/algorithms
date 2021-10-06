import collections

N = int(input())
M = int(input())

graph = collections.defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
visited = []
while stack:
    tmp = stack.pop()
    visited.append(tmp) #사이클 내에 있는 값의 갯수 확인
    for j in graph[tmp]:
        if j not in visited and j not in stack:
            stack.append(j)

print(len(visited)-1)