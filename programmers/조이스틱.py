def solution(name):
    answer = 0
    
    num_list = [min(abs(ord('A')-ord(n)), 26-abs(ord('A')-ord(n))) for n in name]
    #상하
    answer += sum(num_list)
    min_move = len(name) - 1
    
    for i, c in enumerate(name):
        
        next_i = i+1
        
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        #좌우
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)
    
    return answer+min_move
