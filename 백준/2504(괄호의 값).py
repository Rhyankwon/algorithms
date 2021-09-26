import sys

brackets = sys.stdin.readline().strip()

stack = []
info = {')' : '(', ']' : '['}
score = {')' : 2, ']' : 3}

answer = []

result = 0
ex = 0
for i in brackets:
    if i not in info:
        stack.append(i)
    else:
        tmp = 0
        while stack:
            top = stack.pop()
            if top == info[i]:
                if tmp == 0:
                    stack.append(str(score[i]))
                else :
                    stack.append(str(tmp*score[i]))
                break
            elif top.isdigit():
                tmp += int(top)
            else :
                ex = 1
                break
    if ex == 1:
        break

for i in stack:
    if i.isdigit():
        result += int(i)
    else:
        result = 0
        break
print([result, 0][ex==1])