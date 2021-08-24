def solution(relation):
    row = len(relation)
    col = len(relation[0])
    if row == 1:
        return 1
    def dfs(path, column):
        if not column:
            return []
        result = []
        for i in range(len(column)):
            result.append(path+[column[i]])
            result.extend(dfs(path+[column[i]], column[i+1:]))
        return result
    candidates = sorted((dfs([], range(col))), key = lambda x : [len(x), x])
    uniques = []
    for candidate in candidates:
        tmp = [tuple([item[i] for i in candidate]) for item in relation]
        if len(set(tmp)) == row:
            uniques.append(candidate)
    for i in range(len(uniques)):
        for unique in uniques[i+1:]:
            if len(set(uniques[i])) == len(set(uniques[i]) & set(unique)):
                uniques.remove(unique)
    return len(uniques)