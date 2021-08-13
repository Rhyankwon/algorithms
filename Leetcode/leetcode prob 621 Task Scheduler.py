import collections
import pdb
class Solution:
    def leastInterval(self, tasks, n):
        tasks_count = collections.Counter(tasks)
        result = 0
        while True:
            sub_count = n
            for i in tasks_count.most_common(n+1):
                if i[1] != 0 :
                    sub_count -= 1
                    result += 1
                    tasks_count[i[0]] -= 1
            #단 하나도 남지 않았을 때 끝내기.
            #End function when nothing lefts.
            if not any(tasks_count.values()):
                return result
            while sub_count >= 0:
                sub_count -= 1
                result += 1

tasks = ["A","A","A","B","B","B"]
solution = Solution()
print(solution.leastInterval(tasks, 0))

#파이썬 알고리즘 인터뷰의 해설을 참고한 풀이 (80번 문제)
#책에 쓰인대로 실행시간이 길게나와서 카운터 사용을 한차례 줄였더니 40~50%정도 시간 단축됨!.