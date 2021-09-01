import collections

num_test_case = int(input())
answer = []
for i in range(num_test_case):
    num_store = int(input())
    infos = dict()
    stores = []
    for j in range(num_store+2):
        stores.append(list(map(int, input().split())))
    # 시작지점, 편의점들, 끝지점 순서대로 리스트에 저장하기. 0번 인덱스는 시작, -1인덱스는 도착지.
    graph = collections.defaultdict(list)
    for i in range(len(stores)):
        for j in range(len(stores)):
            if i != j:
                val_i = stores[i]
                val_j = stores[j]
                #각 지점마다 근처에 1000m이내로 갈 수 있는 다른 지점들 추가하기.
                if abs(val_i[0]-val_j[0]) + abs(val_i[1]-val_j[1]) <= 1000:
                    graph[i].append(j)
    visited = set()
    stack = [0]
    #시작지점에서부터 갈수 있는 모든 곳을 visited에 추가.
    while stack:
        tmp = stack.pop()
        if tmp in visited:
            continue
        visited.add(tmp)
        for i in graph[tmp]:
            stack.append(i)
    if len(stores)-1 not in visited:
        #마지막 노드(도착지)가 visited에 없으면 return False
        print('sad')
    else:
        print('happy')