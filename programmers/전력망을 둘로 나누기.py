import collections
import sys

def solution(n, wires):
    graph = collections.defaultdict(list)
    nums = [0 for i in range(101)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    while len(graph) > 1:
        candidates = []
        min_num = sys.maxsize
        for i in graph:
            if len(graph[i]) == 1:
                candidates.append(i)
                min_num = min(min_num, nums[i]) #하위 노드 수가 가장 적은 노드에 대해서만 삭제 및 상단 노드로 이동
        for j in candidates:
            if nums[j] == min_num:
                tmp = graph[j].pop()
                graph[tmp].remove(j)
                nums[j] += 1
                nums[tmp] += nums[j]
                del graph[j]
    nums.sort(reverse = True)
    return abs(nums[1] - (n - nums[1]))
