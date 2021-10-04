N = int(input())
answer = -1
def dfs(k, nums):
    global answer
    if len(nums) == k:
            answer += 1
            if answer == N:
                print(nums)
                exit(0)
    else:
        if nums == '':
            for j in range(k-1, 10): #맨 앞자리수는 아무거나 가능.
                dfs(k, str(j))
        else:
            for j in range(k-len(nums)-1, int(nums[-1])): 
                dfs(k, nums+str(j))

for i in range(1, 11): #0부터 9876543210의 경우 까지, 총 10자리수일때까지만 해당 수가 가능하다.
    dfs(i, '')

print('-1')

# 풀이 2 /조합을 이용해서 0, ... 0, 1, 2, ... 2,4,5,6,7 등으로 가능한 모든 조합을 미리 만들고 조건에 맞게 정렬 후 확인하는 방법.
# import itertools

# N = int(input())
# nums = []

# for i in range(1, 11):
#     for j in itertools.combinations(range(10), i):
#         j = sorted(list(j), reverse = True) 
#         nums.append(int(''.join(map(str, j))))
# nums.sort()
# try :
#     print(nums[N])
# except:
#     print(-1)