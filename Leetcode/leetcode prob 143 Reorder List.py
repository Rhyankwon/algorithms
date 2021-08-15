# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        node = None
        # 러너 기법으로 중간값 찾기. 앞쪽부터 중간까지는 정순으로 뒷쪽부터 중간까지는 역으로 정렬해야함.
        # find mid value of the linked list. reverse the list from the end to the middle. 
        while fast and fast.next:
            node, slow, fast = slow, slow.next, fast.next.next
        if not node:
            return
        node.next = None
        queue = collections.deque()
        stack = collections.deque()
        node = head.next
        # 각각 큐, 스택 필요. need queue and stack each.
        while node:
            queue.append(node)
            queue[-1].next, node = None, node.next
        while slow:
            stack.append(slow)
            stack[-1].next, slow = None, slow.next
        node = head
        while True:
            if stack:
                node.next = stack.pop()
                node = node.next
            if queue:
                node.next = queue.popleft()
                node = node.next
            if not stack and not queue:
                break
        # while head:
        #     print(head.val)
        #     head = head.next
        return