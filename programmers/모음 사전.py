def solution(word):
    words = 'AEIOU'
    candidates = []
    def dfs(path):
        if len(path) != 5:
            for i in words:
                if word not in candidates:
                    candidates.append(path+i)
                    if path + i == word:
                        return len(candidates)
                    else :
                        dfs(path+i)
    dfs('')
    return len(candidates)