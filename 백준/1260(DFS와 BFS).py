import collections

N, M, V = map(int, input().split())

graph = collections.defaultdict(list)

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs_ans = []
bfs_ans = []

def dfs(v):
    global dfs_ans
    if v not in dfs_ans: #노드를 아직 지나지 않은 경우에만 답 리스트에 추가
        dfs_ans.append(v)
        if len(dfs_ans) < N: #길이가 N이 되면 끝내기
            for i in sorted(graph[v]):
                dfs(i)

def bfs(v):
    global bfs_ans
    stack = collections.deque()
    stack.append(v)
    while stack:
        tmp = stack.popleft()
        if tmp not in bfs_ans: #아직 방문하지 않은 곳만 답 리스트에 추가 및 재탐색
            bfs_ans.append(tmp)
            for j in sorted(graph[tmp]):
                if j not in stack: #이미 스택에 있으면 안넣기
                    stack.append(j)
            if len(bfs_ans) == N:
                break #길이 끝까지 차면 끝내기

dfs(V)
bfs(V)

for i in dfs_ans: #답안 형식에 맞춰서 출력
    print(i, end = ' ')
print()
for j in bfs_ans:
    print(j, end = ' ')
