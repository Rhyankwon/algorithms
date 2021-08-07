
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        #각 리스트마다 포인터 만들기 / creat pointers for each list
        p1 = p2 = 0
        length = m + n
        merged_list = []
        while p1 < m and p2 < n and len(merged_list) <= length//2:
            if nums1[p1] <= nums2[p2]:
                #만약 리스트2 값이 더 크면 1번 포인터 옮기고 리스트1 값 합병리스트에 추가
                #if value of list2 is bigger then move pointer1 and add value1 to merged list
                merged_list.append(nums1[p1])
                p1 += 1
            elif nums1[p1] > nums2[p2] :
                merged_list.append(nums2[p2])
                p2 += 1
                #한쪽이 먼저 끝난경우 merged_list가 전체 길이 반까지 되도록 다른 리스트에서 충원
                #if a list ends first, fill merged_list by half of total length from another list
        while len(merged_list) <= length//2:
            if p1 < m:
                merged_list.append(nums1[p1])
                p1 += 1
            else :
                merged_list.append(nums2[p2])
                p2 += 1
                #만약 총 길이가 홀수면 리스트 마지막 값, 아니면 마지막 두개의 사이값 리턴
                #if total length is odd then return the last component of merged_list
                #or return the median value of the last both components
        if length%2 != 0:
            return merged_list[-1]
        else :
            return (merged_list[-1]+merged_list[-2])/2

solution = Solution()
nums1 = [7]
nums2 = []
print(solution.findMedianSortedArrays(nums1, nums2))