class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        result = []
        for i in range(len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if queue[0] == i - k :
                queue.pop(0)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result

'''
파이썬 알고리즘 인터뷰 75번 문제.
처음에 안 풀려서 위 책 깃허브에 있는 sohyunwriter님의 코드를 참고했다.
'''