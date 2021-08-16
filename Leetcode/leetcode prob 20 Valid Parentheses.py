class Solution:
    def isValid(self, s):
        bracket = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in s:
            if i in bracket:
                stack.append(i)
            else :
                if stack and  bracket[stack[-1]] == i:
                    stack.pop()
                else :
                    return False
        return not stack