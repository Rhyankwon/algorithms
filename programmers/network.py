import collections

def solution(n, computers):
    answer = 0
    
    visited = [0 for i in range(n)]
    
    for i in range(n):
        if visited[i] == 1: #이미 방문한 경우 패스
            continue
        visited[i] = 1
        answer += 1 #아니면 네트워크 1개추가
        
        stack = collections.deque()
        stack.append(i)
        
        while stack:
            cur = stack.popleft()
            for j, com in enumerate(computers[cur]):
                if com == 1 and visited[j] == 0:
                    visited[j] = 1
                    stack.append(j)        
        
    return answer
