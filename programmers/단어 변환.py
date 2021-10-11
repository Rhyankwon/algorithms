# def solution(begin, target, words):
#     visited = {}
#     for word in words:
#         visited[word] = False
#     queue = [[begin, 0]]
#     while queue:
#         tmp, cnt = queue.pop(0)
#         if tmp == target:
#             return cnt
#         for word in words:
#             if visited[word]:
#                 continue
#             unsimilarity = 0
#             for i in range(len(begin)):
#                 if tmp[i] != word[i]:
#                     unsimilarity += 1
#             if unsimilarity == 1:
#                 visited[word] = True
#                 queue.append([word, cnt+1])
#     return 0

def solution(begin, target, words):
    visited = {}
    for word in words:
        visited[word] = False
    queue = [[begin, 0]]
    while queue:
        tmp, cnt = queue.pop(0)
        if tmp == target:
            return cnt
        for word in words:
            if visited[word]:
                continue
            unsimilarity = 0
            for x, y in zip(tmp, word):
                if x != y:
                    unsimilarity += 1
            if unsimilarity == 1:
                visited[word] = True
                queue.append([word, cnt+1])
    return 0
