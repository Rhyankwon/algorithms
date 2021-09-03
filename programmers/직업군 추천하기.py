import collections

def solution(table, languages, preference):
    dict_preference = collections.defaultdict(int)
    preference_point = {}
    #개발자가 사용할 수 있는 각 언어에 대해 선호도 매치
    for i in range(len(languages)):
        preference_point[languages[i]] = preference[i]
    for language in languages:
        for info in table:
            info = info.split()
            #각 언어별로 각 직업군 점수에 기여하는 만큼 더하기
            if language in info:
                dict_preference[info[0]] += preference_point[language]*(len(info)-info.index(language))
    best = 0
    answer = []
    for job in dict_preference:
        prev_best = best
        # 가장 큰 선호도 값의 키값 확인
        best = max(prev_best, dict_preference[job])
        if best > prev_best:
            answer = []
            answer.append(job)
        # 만약 여러개 같은 값이면 리스트에 모두 저장 후 정렬해서 맨 앞 값 리턴
        elif dict_preference[job] == best:
            answer.append(job)
    return sorted(answer)[0]