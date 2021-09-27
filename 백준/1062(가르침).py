# import itertools   #비트연산자를 이용한 풀이. 당연히 나도 처음부터 생각해낸건 아니고 다른 분의 풀이를 참고했다.
# import sys

# input = sys.stdin.readline

# N, k = map(int, input().strip().split())

# words = []
# for i in range(N):
#     words.append(set(input().strip()))

# common_words = ['a', 'n', 't', 'c', 'i']
# common = []
# for i in common_words:
#     common.append(ord(i)-ord('a'))

# not_common = []
# for i in range(26):
#     if i not in common:
#         not_common.append(i)

# def words_code(w):
#     answer = 0
#     for i in w:
#         if i not in common_words:
#             answer = answer|(1<<(ord(i)-ord('a')))
#     return answer

# if k< 5 or k >= 26:
#     print([0, N][k>=26])
# else:
#     w_code = []
#     for w in words:
#         w_code.append(words_code(w))
#     power_of_2 = [2 ** i for i in not_common]  #특히이부분
#     answer = []
#     for i in itertools.combinations(power_of_2, k-5):
#         num = 0
#         tmp = sum(i)
#         for w in w_code:
#             if w&tmp == w:
#                 num += 1
#         answer.append(num)
#     print(max(answer))


# import collections    #두번째 풀이. dfs를 최적화시킨 풀이. pypy로 해야 풀리는게 아쉽다.
# import sys
# input = sys.stdin.readline

# N, k = map(int, input().split())
# words = []
# for i in range(N):
#     words.append(set(input().strip()))

# learn = [0 for i in range(26)]

# for c in ['a', 'n', 't', 'i', 'c']:
#     learn[ord(c) - ord('a')] = 1
# answer = 0
# def dfs(idx, cnt):
#     if cnt == k-5:
#         global answer
#         num = 0
#         for word in words:
#             check = 0
#             for w in word:
#                 if not learn[ord(w)-ord('a')]:
#                     check = 1
#                     break
#             if check == 0:
#                 num += 1
#         answer = [answer, num][num>answer]
                
#     else:
#         for i in range(idx, 26):
#             if not learn[i]:
#                 learn[i] = 1
#                 dfs(i, cnt+1)
#                 learn[i] = 0


# if k <5 or k >= 26:
#     print([0, N][k>=26])
# else:
#     dfs(0, 0)
#     print(answer)
