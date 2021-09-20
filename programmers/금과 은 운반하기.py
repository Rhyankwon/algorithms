def solution(a, b, g, s, w, timetable):
    min_t = 0
    # max_t = 10 ** (9 + 5 + 1) #최악의 경우 t의범위. 아래처럼 코드를 짜면 매번 a와 b를 감안해서 t의 범위를 정할 수도 있다.
    max_t = (a + b) * max(timetable) * 2
    while max_t > min_t :
        mid_t = min_t + (max_t - min_t) // 2
        carry_g = carry_s = carry = 0
        for i, t in enumerate(timetable):
            num = mid_t // t
            total, sec = num//2, num%2
            total += sec
            if g[i] < w[i] * total:
                carry_g += g[i]
            else :
                carry_g += w[i] * total
            if s[i] < w[i] * total:
                carry_s += s[i]
            else :
                carry_s += w[i] * total
            if s[i] + g[i] < w[i] * total:
                carry += s[i] + g[i]
            else :
                carry += w[i] * total
        if carry_g >= a and carry_s >= b and carry >= a + b:
            answer = mid_t
            max_t = mid_t
        else :
            min_t = mid_t + 1
    return answer
    
