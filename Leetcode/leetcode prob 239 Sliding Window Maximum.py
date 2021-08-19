class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        result = []
        for i in range(len(nums)):
            # 새 값이 들어올 때마다 그것보다 작은것들은 없애버리기.
            # delete components in window smaller than new value.
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            # 큐에 인덱스를 넣어서 인덱스가 k 윈도우크기보다 작으면 제거.
            # use index and queue and delete one if it's smaller than k window.
            if queue[0] == i - k :
                queue.pop(0)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result

'''
파이썬 알고리즘 인터뷰 75번 문제.
처음에 안 풀려서 위 책 깃허브에 있는 sohyunwriter님의 코드를 참고했다.
solution idea is from https://github.com/onlybooks/algorithm-interview/issues/67
'''