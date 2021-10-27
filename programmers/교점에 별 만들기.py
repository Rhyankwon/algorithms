import sys
def solution(line):

    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = -sys.maxsize, -sys.maxsize

    candidates = []
    for i, [a, b, e] in enumerate(line[:-1]):
        for j, [c, d, f] in enumerate(line[i+1:]):
            if a*d - b*c == 0:
                continue
            x, r1 = (b*f-d*e)//(a*d-b*c), (b*f-d*e)%(a*d-b*c)
            y, r2 = (e*c-a*f)//(a*d-b*c), (e*c-a*f)%(a*d-b*c)
            if r1 != 0 or r2 != 0: #나머지 있으면 패스
                continue
            candidates.append([x, y])
            min_x, max_x = [min_x, x][x<min_x], [max_x, x][x>max_x]
            min_y, max_y = [min_y, y][y<min_y], [max_y, y][y>max_y]


    dots = [['.'for i in range(max_x-min_x+1)]for j in range(max_y-min_y+1)] #점으로 구성된 리스트 만들고

    for x, y in candidates:
        print(x-min_x, y-min_y)
        dots[y-min_y][x-min_x] = '*'

    answer = []
    for i in dots[::-1]: #마지막에 각 행 리스트에서 문자열로 합치고 역으로 저장
        answer.append(''.join(i))

    return answer
