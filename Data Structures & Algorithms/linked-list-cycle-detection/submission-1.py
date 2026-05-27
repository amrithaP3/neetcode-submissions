# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next

        # need to make sure that fast.next exists so that
        # fast.next.next is valid 
        # we cannot get .next value of null like if
        # fast.next is null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False