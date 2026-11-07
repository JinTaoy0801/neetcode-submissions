# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        c= 0
        while fast:
            c+=1
            fast = fast.next

        nth = c - n
        if nth == 0:
            return head.next
        curr = head
        count = 0
        while curr.next:
            if count == nth - 1:
                temp = curr.next
                curr.next = temp.next
                temp.next = None
                break

            count+=1
            curr = curr.next
        return head



