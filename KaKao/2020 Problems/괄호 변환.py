def split(p):
    dic1 = {'(' : 0, ')' : 0}
    for i in range(len(p)):
        dic1[p[i]] += 1
        if dic1['('] == dic1[')']:
            dic2 = {'(' : 0, ')' : 0}
            for j in range(i+1, len(p)):
                dic2[p[j]] += 1
            if dic2['('] == dic2[')']:
                break
    return p[:i+1], p[i+1:]
        
def check_right(u):
    stack = []
    for i in range(len(u)):
        if not stack:
            stack.append(u[i])
        elif stack[-1] != u[i] and stack[-1] == '(':
            stack = stack[:-1]
        else :
            stack.append(u[i])
    return True if not stack else False

def solution(p):
    empty_string = ''
    if p == '':
        return p
    u, v = split(p)
    if check_right(u):
        return u + solution(v)
    else :
        empty_string = '(' + solution(v) + ')'
        for i in range(1, len(u)-1):
            if u[i] == ')':
                empty_string += '('
            else :
                empty_string += ')'
        return empty_string