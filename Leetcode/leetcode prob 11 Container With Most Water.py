class Solution:
    def maxArea(self, height):
        left, right = 0, len(height)-1
        volume = 0
        while left < right:
            # volume = max(volume, min(height[right],height[left]) * (right - left))
            if height[left] >= height[right]:
                #원래는 volume을 먼저 계산 후 포인터를 움직였지만 너무 시간이 느리게 나와서
                #min함수라도 줄여보고자 if문 이후에 부피 계산을 했다.
                #I originally calculated volume first and moved pointers but it took too much time
                #min function is unnecessary though it shorten the number of codes, so i removed min.
                volume = max(volume, height[right]*(right-left))
                right -= 1
                #처음에 느리게 나온게 이상해서 혹시나 하고 height에 while문을 넣었다.
                #right포인터를 왼쪽으로 옮겼는데 해당 height가 전보다 작다면 그냥 넘겨도 되니까.
                #그런데 시간이 거의 똑같음. 나중에 그런 케이스가 많은 예제가 추가된다면 효율적인 풀이가 될듯.
                #If height of moved right pointer is shorter than original right height, you can skip.
                #So i added 2 lines but it didnt change amount of function time at all.
                #But it can be more effective if there are cases that are longer.
                # while left < right and height[right] < height[right+1]:
                #     right -= 1
            else :
                volume = max(volume, height[left]*(right-left))
                left += 1
                # while left < right and height[left] < height[left-1]:
                #     left += 1
        return volume

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))