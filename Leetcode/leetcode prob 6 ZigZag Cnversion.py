class Solution:
    def convert(self, s, numRows):
        result = ['']*numRows
        count = 0
        while True:
            #1, 2, 3, 4, 3, 2, 1 식이므로 0~(n-1)까지 반복 후 (n-2)~ 1까지 반복.
            #iterate 0~(n-1) and (n-2)~1.
            for i in range(numRows):
                if count < len(s):
                    result[i] += s[count]
                    count += 1
                else:
                    break
            for i in range(numRows-1, 1, -1):
                #항상 끝나는지 확인. always check if it ends
                if count < len(s):
                    result[i-1] += s[count]
                    count += 1
                else:
                    break
            #끝나면 문자열 리턴. return string when it ends
            if count == len(s):
                return ''.join(result)
            #아래는 리트코드 디스커션에서 본 풀이. 나도 처음에 이런식으로 풀어야지 생각했는데 구현이 쉽지 않았다.
            #이렇게 푸는 방법을 봤으니 앞으로는 아마도 이렇게 할 수 있을듯.
            #그렇게 좋은 문제는 아닌듯. 헷갈리기만 할 뿐 규칙만 찾으면 됨.
        # if numRows <= 1 or numRows >= len(s) :
        #     return s
        # index, step = 0, 1
        # result = [''] * numRows
        # for i in s:
        #     result[index] += i
        #     if index == 0:
        #         step = 1
        #     elif index == numRows-1:
        #         step = -1
        #     index += step
        # return ''.join(result)