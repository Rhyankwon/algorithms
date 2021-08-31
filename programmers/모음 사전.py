def solution(word):
    words = 'AEIOU'
    candidates = []
    def dfs(path):
        if len(path) != 5: #길이 5 이하인 경우만.
            for i in words: #함수 호출할 때마다 모든 단어 반복
                if word not in candidates: #이미 답 찾으면 패스
                    candidates.append(path+i) #아직 답 못찾은경우 후보 리스트에 넣고
                    if path + i == word:  #만약 우리가 원하는 단어 찾으면 재귀 끝내기
                        return
                    else :
                        dfs(path+i)
    dfs('')
    # 답 = 후보 리스트의 길이
    return len(candidates)
