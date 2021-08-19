class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t 문자열에 있는 각 문자의 갯수와 총 갯수 둘다 만족해야함.
        # substring should satiffy both numbers of each letter and the total number.
        count = collections.Counter(t)
        missing = sum(count.values())
        left = right = 0
        start = end = 0
        for right, nums in enumerate(s, 1):
            # right -= 1
            if count[nums] > 0 :
                missing -= 1
            count[nums] -= 1
            if missing == 0:
                while left < right and count[s[left]] < 0:
                    count[s[left]] += 1
                    left += 1
                if not end or (end - start) > (right - left):
                    start, end = left, right
                count[s[left]] += 1
                left += 1
                missing += 1
            # right += 1
        return s[start : end]

'''
파이썬 알고리즘 인터뷰 76번 문제 해설 참고.
예외처리가 아니면 사실 enumerate(s, 1) <- 이렇게 1을 할 필요가 없는데 이걸로 너무 코드가 간결해진다.
'''