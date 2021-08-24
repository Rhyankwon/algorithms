def solution(relation):
    row = len(relation)
    col = len(relation[0])
    def dfs(path, column):
        if not column:
            return []
        result = []
        for i in range(len(column)):
            result.append(path+[column[i]])
            result.extend(dfs(path+[column[i]], column[i+1:]))
        return result
    #조건들로 만들 수 있는 모든 조합 만들고, 길이/번호순서대로 정렬
    candidates = sorted((dfs([], range(col))), key = lambda x : [len(x), x])
    uniques = []
    for candidate in candidates:
        current = [tuple([item[i] for i in candidate]) for item in relation]
        #겹치는게 있나 보고 없으면 후보에 추가 
        if len(set(current)) == row:
            uniques.append(candidate)
    
    for i in range(len(uniques)):
        for unique in uniques[i+1:]:
            #앞쪽부터 짧은거~긴것 순서대로 있으니까 앞쪽부터 반복하면서 뒷쪽에 
            #앞쪽 후보를 포함하는게 있는지 확인. 있으면 뒷쪽거(더 큰 집합) 제거
            if len(set(uniques[i])) == len(set(uniques[i]) & set(unique)):
                uniques.remove(unique)
    return len(uniques)