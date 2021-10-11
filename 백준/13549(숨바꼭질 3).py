import sys
import heapq

N, K = map(int, input().split())

answer = sys.maxsize
stack = [[0, N]]
visited = [False for i in range(100001)]

while stack:
    num, tmp = heapq.heappop(stack)
    visited[tmp] = True
    if tmp == K:
        print(num)
        exit(0)
    if tmp-1 >= 0 and tmp-1 < 100001 and not visited[tmp-1]:
        heapq.heappush(stack, [num+1, tmp-1])
    if tmp+1 >= 0 and tmp+1 < 100001 and not visited[tmp+1]:
        heapq.heappush(stack, [num+1, tmp+1])
    if tmp*2 >= 0 and tmp*2 < 100001 and not visited[tmp*2]:
        heapq.heappush(stack, [num, tmp*2])