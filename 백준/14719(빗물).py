H, W = map(int, input().split())

blocks = list(map(int, input().split()))
max_height = 0
blocks_left = [] 
water = 0
for i in range(len(blocks)):
    while blocks_left and blocks[blocks_left[-1]] < blocks[i]:
        top = blocks_left.pop()
        if not blocks_left:
            break
        water += (min(blocks[i], blocks[blocks_left[-1]]) - blocks[top]) * \
                 (i - blocks_left[-1]-1)
    blocks_left.append(i)
print(water)