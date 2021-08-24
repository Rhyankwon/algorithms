#2019 카카오 블라인드 채용 4번 문제(무지의 먹방 라이브) 파이썬 해설 1
#효율성 테스트 통과x. 정확성은 통과o

# def solution(food_times, k):
#     time = 0
#     count = {}
#     while True:
#          #매번 food 테이블을 한 바퀴씩 반복하는데, 이미 음식이 0인 부분은 패스.
#         for i in range(len(food_times)):
#             if food_times[i] == 0:
#                 count[i] = 1
#                 #테이블이 모두 빈 경우 -1 리턴.
#                 if len(count) == len(food_times):
#                     return -1
#                 continue
#             #음식이 있는 경우, 그 때 시간이 k면 인덱스 리턴, 아니면 음식-1, 시간+1
#             if time == k:
#                 return i+1
#             food_times[i] -= 1
#             time += 1
            
    
#2019 카카오 블라인드 채용 4번 문제(무지의 먹방 라이브) 해설 2
#효율성 테스트 통과o, 정확성 통과 o
import collections
import heapq

def solution(food_times, k):
    #음식이 없는 경우 -1 리턴
    if not food_times:
        return -1
    foods = []
    for i in range(len(food_times)):
        heapq.heappush(foods, [food_times[i], i+1])
    food = 0
    while (foods[0][0] - food) * len(foods) <= k:
        #food는 앞쪽에서 전체음식을 먹은 횟수. 가령 테이블을 3바퀴 돌았으면 그 다음 음식은 5가 들어있더라도 2만큼만 계산해야하니까.
        k -= (foods[0][0] - food) * len(foods)
        food += (foods[0][0] - food)
        cur = foods[0][0]
        #foods에서 음식 수가 같은 경우 그것들을 다 빼야하니깐.
        while foods[0][0] == cur :
            heapq.heappop(foods)
            #만약 k가 남아있는데 foods가 끝나면 -1리턴.
            #k가 0인 경우도, 그 다음에 올 인덱스를 반환하는게 맞으므로 그 때 foods가 빈 경우는 -1을 리턴해야함.
            if not foods:
                return -1
    foods.sort(key = lambda x : x[1]
    return foods[k%len(foods)][1]

'''
무지의 먹방 라이브 테스트케이스. 이 문제는 첫번째 풀이로 했을 땐 이렇게 많은 테스트케이스의 도움따위 필요없이
잘 풀었었는데 두번째 풀이를 할 때에는 뭔가 도움이 많이 됐다. 특히 1, 2, 4번이 도움이 많이 됐다.

#1 답 = 1
nums =[3, 1, 2]
print(solution(nums, 5))
#2 답 = 2, 출처 : https://programmers.co.kr/questions/12975
nums =[7,8,3,3,2,2,2,2,2,2,2,2]
print(solution(nums, 35))
#3 답 = 6, 출처 : https://programmers.co.kr/questions/10851
nums = [1, 5, 5, 5, 5, 6, 7]
print(solution(nums, 31))
#4 답 = -1
nums = [4]
print(solution(nums, 6))
#5 답 = -1
nums = []
print(solution(nums, 2))
'''
