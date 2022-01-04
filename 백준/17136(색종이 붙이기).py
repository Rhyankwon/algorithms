import sys

grid = []

for i in range(10):
    grid.append(list(map(int, input().split())))

def func(x, y, cnt):
    global result
    if y >= 10:
        result = min(cnt, result)
    elif x >= 10:
        func(0, y+1, cnt)
    elif grid[x][y] == 1:
        for i in range(5):
            if paper[i] == 5:
                continue
            if x+i >= 10 or y+i >= 10:
                continue
            flag = 0
            for k in range(i+1):
                for j in range(i+1):
                    if grid[x+k][y+j] == 0:
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                for k in range(i+1):
                    for j in range(i+1):
                        grid[x+k][y+j] = 0
                paper[i] += 1
                func(x+i+1, y, cnt+1)
                paper[i] -= 1
                for k in range(i+1):
                    for j in range(i+1):
                        grid[x+k][y+j] = 1
    else :
        func(x+1, y, cnt)
result = sys.maxsize       
paper = [0 for i in range(5)]
func(0, 0, 0)
print(result if result != sys.maxsize else -1)