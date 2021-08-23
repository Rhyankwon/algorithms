import collections
import pdb
class Solution:
    def newsClustering(self, str1, str2):
        def makeSet(strs):
            result = []
            strs = strs.lower()
            for i in range(1, len(strs)):
                prev = strs[i-1:i+1]
                # 두글자씩 슬라이싱 후 문자로만 구성됐는지 확인
                if prev.isalpha():
                    result.append(prev)
            return result
        l1 = l2 = 0
        #두 문자열을 2단어 이중집합으로 만든 뒤 정렬
        str1_set = sorted(makeSet(str1))
        str2_set = sorted(makeSet(str2))
        ans = 65536
        #inter = 교집합, union = 합집합
        inter = union = 0
        while True:
            if not (str1_set and str2_set):
                #둘 다 없으면 합집합도 0. 그런 경우 ans 리턴, 아니면 0 반환
                union = len(str1_set) + len(str2_set)
                if union == 0:
                    return ans
                else :
                    return 0
            if l1 <= len(str1_set) - 1 and l2 <= len(str2_set) - 1:
                union += 1
                #투포인터. 두 값 같으면 교,합집합 둘다+1, 다르면 합집합만+1 
                if str1_set[l1] == str2_set[l2]:
                    inter += 1
                    l1 += 1
                    l2 += 1
                elif str1_set[l1] > str2_set[l2]:
                    l2 += 1
                else :
                    l1 += 1
            #남은 리스트는 모두 합집합 갯수로 추가
            elif l1 == len(str1_set):
                while l2 <= len(str2_set) - 1:
                    union += 1
                    l2 += 1
                break
            elif l2 == len(strs2_set):
                while l1 <= len(str1_set) - 1:
                    union += 1
                    l1 += 1
                break
        ans *= (inter/union)
        return int(ans)

solution = Solution()
prob1 = ['FRANCE', 'FRENCH']
prob2 = ['handshake', 'shake hands']
prob3 = ['aa1+aa2', 'AAAA12']
prob4 = ['E=M*C^2', 'e=m*c^2']
print(solution.newsClustering(prob1[0], prob1[1]))
print(solution.newsClustering(prob2[0], prob2[1]))
print(solution.newsClustering(prob3[0], prob3[1]))
print(solution.newsClustering(prob4[0], prob4[1]))