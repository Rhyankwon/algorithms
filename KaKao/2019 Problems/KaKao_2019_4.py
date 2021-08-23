#2019 카카오 블라인드 채용 4번 문제(무지의 먹방 라이브)
#효율성 테스트 통과x. 정확성은 통과o

def solution(food_times, k):
    time = 0
    count = {}
    while True:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                count[i] = 1
                if len(count) == len(food_times):
                    return -1
                continue
            if time == k:
                return i+1
            food_times[i] -= 1
            time += 1