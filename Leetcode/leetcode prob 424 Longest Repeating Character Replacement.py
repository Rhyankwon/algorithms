class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        count = collections.Counter()
        for right in range(len(s)):
            count[s[right]] += 1
            #새로운 값이 추가되면 조건 만족하는지 다시 확인.
            #adding a new value, check if window meets prob requirement.
            while right - left + 1 - count.most_common(1)[0][1] > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result
        # 아래는 파이썬 알고리즘 인터뷰 풀이. 어차피 길이만 알면 되니까 가능한 풀이! Nice
        #     if right - left + 1 - count.most_common(1)[0][1] > k:
        #         count[s[left]] -= 1
        #         left += 1
        # return right - left + 1

'''
파이썬 알고리즘 인터뷰 77번 해설 참고
윈도우 길이 - 가장 많은 문자의 갯수 = k 라는 걸 감안하면 풀 수 있다.
length of window - most frequently qppearing letter = k.
'''
