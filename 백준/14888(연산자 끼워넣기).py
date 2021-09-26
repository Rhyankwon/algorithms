# import sys  #첫번째 풀이. eval을 과하게 써서 안풀림

# N = int(input())
# nums = list(map(int, input().split()))
# num_ops = list(map(int, input().split()))

# op_candidates = '+-*/'
# ops = []
# for i, op in enumerate(op_candidates):
#     ops.extend([op] * num_ops[i])

# op_comb = set()
# def dfs(path, op_, k):
#     if k == 0:
#         global op_comb
#         op_comb.add(tuple(path))
#     else:
#         for i in range(k):
#             dfs(path+[op_[i]], op_[:i]+op_[i+1:], k-1)

# dfs([], ops, N-1)

# min_ans = sys.maxsize
# max_ans = -sys.maxsize

# for op in op_comb:
#     tmp = str(nums[0])
#     answer = ''
#     for i in range(N-1):
#         answer = str(op[i])
#         answer += str(nums[i+1])
#         tmp = int(eval(str(tmp)+answer))
#     if tmp < min_ans:
#         min_ans = tmp
#     if tmp > max_ans:
#         max_ans = tmp

# print(max_ans)
# print(min_ans)

# import sys   #두번째 풀이. 풀리긴 하는데 어마어마한 속도가 걸림; dfs가 문제.

# N = int(input())
# nums = list(map(int, input().split()))
# num_ops = list(map(int, input().split()))

# op_candidates = '+-*/'
# ops = []
# for i, op in enumerate(op_candidates):
#     ops.extend([op] * num_ops[i])

# min_ans = sys.maxsize
# max_ans = -sys.maxsize

# op_comb = set()
# def dfs(op_, k, ans):
#     if k == N:
#         global min_ans
#         global max_ans
#         if ans < min_ans:
#             min_ans = ans
#         if ans > max_ans:
#             max_ans = ans
#     else:
#         for i in range(N-k):
#             if op_[i] == '+':
#                 val = ans+nums[k]
#             elif op_[i] == '-':
#                 val = ans-nums[k]
#             elif op_[i] == '*':
#                 val = ans*nums[k]
#             else:
#                 val = int(ans/nums[k])
#             dfs(op_[:i]+op_[i+1:], k+1, val)

# dfs(ops, 1, nums[0])

# print(max_ans)
# print(min_ans)

# import sys   #세번째 풀이. itertools를 굳이 안 쓰려고 했엇지만 속도 단축을 위해 사용. 시간 약 1/10로 단축.
# import itertools
# N = int(input())
# nums = list(map(int, input().split()))
# num_ops = list(map(int, input().split()))

# op_candidates = '+-*/'
# ops = []
# for i, op in enumerate(op_candidates):
#     ops.extend([op] * num_ops[i])

# op_comb = set(itertools.permutations(ops, N-1))

# min_ans = sys.maxsize
# max_ans = -sys.maxsize
# candidates = []
# for op in op_comb:
#     val = nums[0]
#     for i in range(N-1):
#         if op[i] == '+':
#             val = (val+nums[i+1])
#         elif op[i] == '-':
#             val = (val-nums[i+1])
#         elif op[i] == '*':
#             val = (val*nums[i+1])
#         else:
#             val = int(val/nums[i+1])
#     candidates += [val]

# print(max(candidates))
# print(min(candidates))


# import sys;ins=sys.stdin.readline  #네번째 풀이 내 코드x (https://www.acmicpc.net/source/10486639). dfs안에 for문/비교구문/if문 등이 현저히 적어 속도를 거의 1/100로 단축할 수 있다.
# N = int(ins())
# nums = list(map(int, ins().split()))
# a,b,c,d = map(int,ins().split())
# ans = []

# def step(cur,i,a,b,c,d):
#     if i==N: ans.append(cur);return # haha....
#     n = nums[i]
#     if a!=0: step(cur+n,i+1,a-1,b,c,d)
#     if b!=0: step(cur-n,i+1,a,b-1,c,d)
#     if c!=0: step(cur*n,i+1,a,b,c-1,d)
#     if d!=0: step(int(cur/n),i+1,a,b,c,d-1)
        
# step(nums[0],1,a,b,c,d)
# print(max(ans),min(ans))
