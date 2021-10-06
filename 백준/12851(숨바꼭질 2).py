import sys  #풀이. 우선순위큐를 사용한 풀이, 916ms 속도.
import heapq

N, K = map(int, input().split())

answer = sys.maxsize
cnt = 0
stack = [[0, N]]
visited = [False for i in range(100001)]

while stack:
    num, tmp = heapq.heappop(stack)
    if num > answer: #앞서 계산된 최소 연산횟수보다 커지면 루프 탈출
        break
    visited[tmp] = True
    if tmp == K:
        if answer > num :
            answer = num
            cnt = 1
        elif answer == num: #연산횟수가 동일할 시 경우의수 하나 추가.
            cnt += 1
    if tmp-1 >= 0 and tmp-1 < 100001 and not visited[tmp-1]:
        heapq.heappush(stack, [num+1, tmp-1])
    if tmp+1 >= 0 and tmp+1 < 100001 and not visited[tmp+1]:
        heapq.heappush(stack, [num+1, tmp+1])
    if tmp*2 >= 0 and tmp*2 < 100001 and not visited[tmp*2]:
        heapq.heappush(stack, [num+1, tmp*2])

print(answer)
print(cnt)

# import sys   #두번째 풀이. 힙이 아니라 덱을 사용했다. 나머지 코드는 전부 동일, 속도는 736ms로 다소 감소
# import collections

# N, K = map(int, input().split())

# answer = sys.maxsize
# cnt = 0
# stack = collections.deque()
# stack.append([0, N])
# visited = [False for i in range(100001)]

# while stack:
#     num, tmp = stack.popleft()
#     if num > answer:
#         break
#     visited[tmp] = True
#     if tmp == K:
#         if answer > num :
#             answer = num
#             cnt = 1
#         elif answer == num:
#             cnt += 1
#     if tmp-1 >= 0 and tmp-1 < 100001 and not visited[tmp-1]:
#         stack.append([num+1, tmp-1])
#     if tmp+1 >= 0 and tmp+1 < 100001 and not visited[tmp+1]:
#         stack.append([num+1, tmp+1])
#     if tmp*2 >= 0 and tmp*2 < 100001 and not visited[tmp*2]:
#         stack.append([num+1, tmp*2])

# print(answer)
# print(cnt)