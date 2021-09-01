import collections

num_city = int(input())
num_plans = int(input())
graph = collections.defaultdict(list)
for i in range(num_city):
    info = list(map(int, input().split()))
    for j in range(len(info)):
        if info[j] != 0:
            graph[i+1].append(j+1)
cities = list(map(int, input().split()))
# 윗쪽까진 입력. 입력 받으면서 연결되있는 간선 추가하기
stack = []
stack.append(cities[0])
visited = set()
while stack:
    cur = stack.pop()
    if cur not in visited:
        visited.add(cur)
        #연결됀 부분은 visited에 추가하기. 연결돼있기만 하면 여행가능하다.
        candidates = graph[cur]
        for j in candidates:
            if j not in stack:
                stack.append(j)
if visited & set(cities) == set(cities):
    #visited집합 안에 cities(여행해야 하는 곳들) 포함돼있으면 yes 리턴한다.
    print('YES')
else :
    print('NO')