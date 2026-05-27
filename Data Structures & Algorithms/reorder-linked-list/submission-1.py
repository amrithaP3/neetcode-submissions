# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first half and second half of list
        # reverse second portion
        # one from first half, one from second half reversed, and so on

        slow, fast = head, head.next

        # slow pointer will point to middle of the list 
        # slow = end of first half!
        # slow.next = beginning of second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of LL
        # prev = head of new LL
        prev, second = None, slow.next

        # this is required bc splitting into 2 diff. lists
        # slow is part of first list so its next value should be None
        # to signify the end of first list
        slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # reorder/merge the two halves
        first, second = head, prev
        while second:
            # storing bc breaking and modifying those links in each LL
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        








        
        
        
        
        


