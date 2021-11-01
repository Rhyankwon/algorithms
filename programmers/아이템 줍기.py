def solution(rectangle, characterX, characterY, itemX, itemY):
    edges = set()
    inside = set()
    for lx, ly, rx, ry in rectangle:
        for x in range(2*lx, 2*rx+1):
            for y in range(2*ly, 2*ry+1):
                if x == 2*lx or x == 2*rx or y == 2*ly or y == 2*ry:
                    edges.add((x/2, y/2))
                else:
                    inside.add((x/2,y/2))
    edges = edges - inside
    start = (characterX, characterY)
    end = (itemX, itemY)
    dir = [[0.5, 0], [0, 0.5], [-0.5, 0], [0, -0.5]]
    tmp = start
    cnt = end_cnt = 0
    while True:
        if tmp == end:
            end_cnt = cnt
        try:
            edges.remove(tmp)
        except:
            break
        x, y = tmp
        if x == int(x) and y == int(y):
            cnt += 1
        for dx, dy in dir:
            if (x+dx, y+dy) in edges:
                tmp = (x+dx, y+dy)
                break
    return min(end_cnt, cnt - end_cnt)