import pdb
class Solution:
    def longestPalindrome(self, s):
        def ispalindrome(index1, index2):
            while index1 >= 0 and index2 <= len(s) and s[index1] == s[index2-1]:
                #길이가 1인 경우의 확인을 위해 index2-1부터 확인 후 확장.
                #to check string shorter than 1, check from index2-1 and expand
                index1 -= 1
                index2 += 1
            return s[index1+1:index2-1]
        #파이썬 알고리즘 인터뷰 159쪽 풀이와 비교하면, 길이 2보다 작은 경우의 예외처리를 생략.
        result = ''
        for i in range(len(s)):
            #팰린드롬은 짝수일수도, 홀수일수도. i+1과 i+2 모두 확인한다.
            #palindrome can be either odd or even so check both i+1 and i+2
            result = max(result, \
            ispalindrome(i, i+1), ispalindrome(i, i+2), key = len)
        return result

solution = Solution()
print(solution.longestPalindrome('aabbsdfadfgggggb'))

#파이썬 알고리즘 인터뷰 6번 문제
