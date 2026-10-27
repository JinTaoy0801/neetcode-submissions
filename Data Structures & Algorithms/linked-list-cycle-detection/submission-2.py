# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, start = head, head
        while start and start.next:
            slow = slow.next
            start = start.next.next
            if slow == start:
                return True

        return False