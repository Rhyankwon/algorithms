N = int(input())
answer = []
for i in range(N):
    words = input()
    start = [0, 0]
    indices = [[0, 0]]
    cur = 0
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for i in words:
        if i == 'F':
            for i, [j, k] in enumerate(zip(start, dir[cur])):
                start[i] = j+k
            indices.append(start[:])
        elif i == 'B':
            for i, [j, k] in enumerate(zip(start, dir[cur])):
                start[i] = j-k
            indices.append(start[:])
        elif i == 'L':
            cur = (cur-1)%4
        elif i == 'R':
            cur = (cur+1)%4

    indices = (list(zip(*indices)))
    left, right = min(indices[0]), max(indices[0])
    down, up = min(indices[1]), max(indices[1])
    answer.append((right-left) * (up-down))

for a in answer:
    print(a)