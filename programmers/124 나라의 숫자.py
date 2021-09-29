def solution(n):
    answer = ''
    while n:
        quo, rem = divmod(n, 3)
        answer = '412'[rem] + answer
        if rem == 0:
            quo -= 1 #나머지0인 경우 이미 값 처리 했으므로 몫에서 1빼준다
        n = quo
    return answer
