# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        slow, fast = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        curr = head
        while prev.next:
            temp = curr.next
            temp2 = prev.next
            curr.next = prev
            prev.next = temp
            curr = temp
            prev = temp2
            

        


        